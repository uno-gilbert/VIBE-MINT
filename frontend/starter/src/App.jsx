import { useAccount, useConnect, useDisconnect, useWriteContract, useWaitForTransactionReceipt } from "wagmi";
import { parseEther } from "viem";
import { vibeMintAbi, CONTRACT_ADDRESS } from "./contract.js";

function App() {
  const { address, isConnected, chainId } = useAccount();
  const { connect, connectors, isPending: isConnecting } = useConnect();
  const { disconnect } = useDisconnect();

  const { writeContract, data: hash, isPending, error } = useWriteContract();
  const { isLoading: isConfirming, isSuccess } = useWaitForTransactionReceipt({ hash });

  const sepoliaId = 11155111;
  const isSepolia = chainId === sepoliaId;
  const hasAddress = CONTRACT_ADDRESS && CONTRACT_ADDRESS !== "undefined";

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
      {isSuccess && <p className="success">Mint 성공! Etherscan에서 tx 확인하세요.</p>}
      {hash && <p className="status">Tx: {hash.slice(0, 10)}…</p>}
    </div>
  );
}

export default App;
