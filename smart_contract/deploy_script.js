// Sample deployment script using Hardhat and ethers.js.
// Ensure you have Hardhat installed and configured in your project.
const hre = require("hardhat");

async function main() {
  const AutoSentry = await hre.ethers.getContractFactory("AutoSentry");
  const autosentry = await AutoSentry.deploy();
  await autosentry.deployed();
  console.log("AutoSentry deployed to:", autosentry.address);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
