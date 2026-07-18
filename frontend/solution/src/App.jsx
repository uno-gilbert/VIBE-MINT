import {
  useAccount,
  useConnect,
  useDisconnect,
  useReadContract,
  useSwitchChain,
  useWriteContract,
  useWaitForTransactionReceipt,
} from "wagmi";
import { formatEther, parseEther } from "viem";
import { useState } from "react";
import { vibeMintAbi, CONTRACT_ADDRESS } from "./contract.js";
import { SEPOLIA_CHAIN_ID } from "./wagmi.js";
import { TxHashLink } from "./TxHashLink.jsx";
import { HeroCardPreview } from "./HeroCardPreview.jsx";

function App() {
  const { address, isConnected, chainId } = useAccount();
  const { connect, connectors, isPending: isConnecting } = useConnect();
  const { disconnect } = useDisconnect();
  const { switchChain, isPending: isSwitching } = useSwitchChain();

  const hasAddress =
    CONTRACT_ADDRESS &&
    CONTRACT_ADDRESS !== "undefined" &&
    CONTRACT_ADDRESS.startsWith("0x") &&
    CONTRACT_ADDRESS.length === 42;

  const isSepolia = chainId === SEPOLIA_CHAIN_ID;

  const { data: totalMinted, refetch: refetchSupply } = useReadContract({
    address: hasAddress ? CONTRACT_ADDRESS : undefined,
    abi: vibeMintAbi,
    functionName: "totalMinted",
  });

  const { data: maxSupply } = useReadContract({
    address: hasAddress ? CONTRACT_ADDRESS : undefined,
    abi: vibeMintAbi,
    functionName: "maxSupply",
  });

  const { data: mintPrice } = useReadContract({
    address: hasAddress ? CONTRACT_ADDRESS : undefined,
    abi: vibeMintAbi,
    functionName: "mintPrice",
  });

  const { data: publicMintEnabled } = useReadContract({
    address: hasAddress ? CONTRACT_ADDRESS : undefined,
    abi: vibeMintAbi,
    functionName: "publicMintEnabled",
  });

  const { data: walletMinted } = useReadContract({
    address: hasAddress ? CONTRACT_ADDRESS : undefined,
    abi: vibeMintAbi,
    functionName: "mintedCount",
    args: address ? [address] : undefined,
  });

  const { data: isWhitelisted } = useReadContract({
    address: hasAddress ? CONTRACT_ADDRESS : undefined,
    abi: vibeMintAbi,
    functionName: "whitelist",
    args: address ? [address] : undefined,
  });

  const { writeContract, data: hash, isPending, error, reset } = useWriteContract();
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
  const [lookupId, setLookupId] = useState("");

  const priceWei = mintPrice ?? parseEther("0.001");
  const priceLabel = formatEther(priceWei);

  const mint = (fn) => {
    reset();
    writeContract({
      address: CONTRACT_ADDRESS,
      abi: vibeMintAbi,
      functionName: fn,
      value: priceWei,
      gas: 250_000n,
    });
  };

  const etherscanNftUrl =
    hasAddress && totalMinted !== undefined && Number(totalMinted) > 0
      ? `https://sepolia.etherscan.io/nft/${CONTRACT_ADDRESS}/${Number(totalMinted) - 1}`
      : null;

  return (
    <div className="card">
      <h1>
        VibeMint
        <span className="badge">Sepolia</span>
      </h1>
      <p>쉽게 이해하고 빠르게 AI 바이브 코딩으로 만들어 보는 NFT</p>

      {!hasAddress && (
        <p className="error">`.env`에 `VITE_CONTRACT_ADDRESS`를 설정하세요.</p>
      )}

      {!isConnected ? (
        <button
          disabled={isConnecting}
          onClick={() => connect({ connector: connectors[0] })}
        >
          Connect MetaMask
        </button>
      ) : (
        <>
          <p className="status">
            {address?.slice(0, 6)}…{address?.slice(-4)}
          </p>

          {!isSepolia && (
            <button
              className="outline"
              disabled={isSwitching}
              onClick={() => switchChain({ chainId: SEPOLIA_CHAIN_ID })}
            >
              Switch to Sepolia
            </button>
          )}

          <button className="secondary" onClick={() => disconnect()}>
            Disconnect
          </button>

          {hasAddress && isSepolia && (
            <>
              <div className="stats">
                <div className="stat">
                  Minted
                  <strong>
                    {totalMinted !== undefined ? Number(totalMinted) : "—"} /{" "}
                    {maxSupply !== undefined ? Number(maxSupply) : "100"}
                  </strong>
                </div>
                <div className="stat">
                  Your mints
                  <strong>{walletMinted !== undefined ? Number(walletMinted) : "—"} / 3</strong>
                </div>
                <div className="stat">
                  Price
                  <strong>{priceLabel} ETH</strong>
                </div>
                <div className="stat">
                  Public mint
                  <strong>{publicMintEnabled ? "ON" : "OFF"}</strong>
                </div>
              </div>

              <div className="actions">
                <button
                  disabled={
                    !publicMintEnabled || isPending || isConfirming
                  }
                  onClick={() => mint("mint")}
                >
                  {isPending || isConfirming ? "Confirm in wallet…" : `Public Mint (${priceLabel} ETH)`}
                </button>

                {isWhitelisted && (
                  <button
                    disabled={isPending || isConfirming}
                    onClick={() => mint("whitelistMint")}
                  >
                    Whitelist Mint ({priceLabel} ETH)
                  </button>
                )}
              </div>

              {etherscanNftUrl && (
                <p className="status">
                  <a href={etherscanNftUrl} target="_blank" rel="noreferrer">
                    Etherscan NFT (latest token)
                  </a>
                </p>
              )}
            </>
          )}
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

      {hasAddress && totalMinted !== undefined && Number(totalMinted) > 0 && (
        <section className="hero-lookup">
          <label htmlFor="token-lookup">다른 tokenId 미리보기</label>
          <div className="hero-lookup__row">
            <input
              id="token-lookup"
              type="number"
              min={0}
              max={Math.max(0, Number(totalMinted) - 1)}
              placeholder="0"
              value={lookupId}
              onChange={(e) => setLookupId(e.target.value)}
            />
            <button
              type="button"
              className="outline"
              onClick={() => {
                const id = Number(lookupId);
                if (!Number.isNaN(id) && id >= 0 && id < Number(totalMinted)) {
                  setPreviewTokenId(id);
                }
              }}
            >
              보기
            </button>
          </div>
        </section>
      )}

      <p className="status" style={{ marginTop: "1.5rem", fontSize: "0.75rem" }}>
        테스트넷 교육용 — 메인넷 배포 전 전문 Audit 필수
      </p>
    </div>
  );
}

export default App;
