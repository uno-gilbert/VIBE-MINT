const SEPOLIA_TX_URL = "https://sepolia.etherscan.io/tx";

export function TxHashLink({ hash }) {
  if (!hash) return null;

  const start = hash.slice(0, 3);
  const end = hash.slice(-3);
  const middle = hash.slice(3, -3);

  return (
    <p className="success mint-success">
      Mint 성공!{" "}
      <a
        className="tx-link"
        href={`${SEPOLIA_TX_URL}/${hash}`}
        target="_blank"
        rel="noreferrer"
        title="Sepolia Etherscan에서 트랜잭션 보기"
      >
        <span className="tx-hash">
          <span className="tx-hash-em">{start}</span>
          {middle}
          <span className="tx-hash-em">{end}</span>
        </span>
      </a>
    </p>
  );
}
