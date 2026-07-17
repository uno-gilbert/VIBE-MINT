import {
  useAccount,
  useConnect,
  useDisconnect,
  useReadContract,
  useWriteContract,
  useWaitForTransactionReceipt,
} from "wagmi";
import { parseEther } from "viem";
import { useState } from "react";
import { vibeMintAbi, CONTRACT_ADDRESS } from "./contract.js";
import { TxHashLink } from "./TxHashLink.jsx";
import { HeroCardPreview } from "./HeroCardPreview.jsx";

function App() {
  const { address, isConnected, chainId } = useAccount();
  const { connect, connectors, isPending: isConnecting } = useConnect();
  const { disconnect } = useDisconnect();

  const hasAddress = CONTRACT_ADDRESS && CONTRACT_ADDRESS !== "undefined";

  const { data: totalMinted, refetch: refetchSupply } = useReadContract({
    address: hasAddress ? CONTRACT_ADDRESS : undefined,
    abi: vibeMintAbi,
    functionName: "totalMinted",
  });

  const { writeContract, data: hash, isPending, error } = useWriteContract();
  const { isLoading: isConfirming, isSuccess } = useWaitForTransactionReceipt({
    hash,
    query: {
      onSuccess: async () => {
        const result = await refetchSupply();
        const minted = result.data;
        if (minted !== undefined && Number(minted) > 0) {
          setPreviewTokenId(Number(minted) - 1);
        }
      },
    },
  });

  const [previewTokenId, setPreviewTokenId] = useState(null);

  const sepoliaId = 11155111;
  const isSepolia = chainId === sepoliaId;

  const handleMint = () => {
    if (!hasAddress) return;
    writeContract({
      address: CONTRACT_ADDRESS,
      abi: vibeMintAbi,
      functionName: "mint",
      value: parseEther("0.001"),
    });
  };

  return (
    <div className="card">
      <h1>VibeMint</h1>
      <p>AI 바이브 코딩 NFT Mint (교육용 · Sepolia)</p>

      {!hasAddress && (
        <p className="error">
          .env에 VITE_CONTRACT_ADDRESS를 설정하세요.
        </p>
      )}

      {!isConnected ? (
        <button
          disabled={isConnecting}
          onClick={() => connect({ connector: connectors[0] })}
        >
          Connect Wallet
        </button>
      ) : (
        <>
          <p className="status">
            {address?.slice(0, 6)}…{address?.slice(-4)}
            {!isSepolia && " — Sepolia로 전환 필요"}
          </p>
          <button className="secondary" onClick={() => disconnect()}>
            Disconnect
          </button>
          <div style={{ marginTop: "1rem" }}>
            <button
              disabled={!isSepolia || !hasAddress || isPending || isConfirming}
              onClick={handleMint}
            >
              {isPending || isConfirming ? "Minting…" : "Mint (0.001 ETH)"}
            </button>
          </div>
        </>
      )}

      {error && <p className="error">{error.shortMessage ?? error.message}</p>}
      {isSuccess && hash && <TxHashLink hash={hash} />}

      {previewTokenId !== null && (
        <section className="hero-section">
          <h2>내 Hero 카드 (DApp 미리보기)</h2>
          <HeroCardPreview tokenId={previewTokenId} />
        </section>
      )}
    </div>
  );
}

export default App;
