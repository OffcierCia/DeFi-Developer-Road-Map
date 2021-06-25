# 디파이 개발자 로드맵

**여기서 최고의 디파이 & 블록체인 연구 그리고 툴을 수집하고 의논합니다. - 기여는 환영합니다.**

**작은 수정 사항부터 번역, 문서, 툴 등 자유롭게 풀 요청을 제출해주세요.**

[![Support Project](https://img.shields.io/badge/Support-Project-critical)](https://github.com/OffcierCia/DeFi-Developer-Road-Map#support-project) [![Research Base](https://img.shields.io/badge/Research-Base-lightgrey )](https://github.com/OffcierCia/ultimate-defi-research-base) [![Supported by LEGO](https://img.shields.io/badge/Supported%20by-LEGO-%2300A3FF)](https://www.notion.so/LEGO-Lido-Ecosystem-Grants-Organisation-d7f0bf0182d44348b6173639d2e8363d) [![Mail](https://img.shields.io/badge/Mail-offcierciapr%40protonmail.com-brightgreen)](mailto:offcierciapr@protonmail.com) 


<details>
<summary>번역</summary>
<br>
 <a href="translations/README_guj.md">구자라트어(Gujarati)</a>
 <a href="translations/README_ko.md">한국어(Korean)</a>
</details>

## 로드맵

![Roadmap](../DeFiDevRroadMap_-Page-1.svg)

# Navigation

|       Topic      | Instant Link                                                                                                              |
|:----------------:|---------------------------------------------------------------------------------------------------------------------------|
| Basics           | [Explore](https://github.com/OffcierCia/DeFi-Developer-Road-Map#basics)                                                   |
| dApps            | [Explore](https://github.com/OffcierCia/DeFi-Developer-Road-Map#dapps)                                                    |
| Frameworks       | [Explore](https://github.com/OffcierCia/DeFi-Developer-Road-Map#frameworks)                                               |
| zk-snarks        | [Explore](https://github.com/OffcierCia/DeFi-Developer-Road-Map#zk-snarks)                                                |
| Further Readings | [Explore](https://github.com/OffcierCia/DeFi-Developer-Road-Map#further-readings)                                         |
| Security         | [Explore](https://github.com/OffcierCia/DeFi-Developer-Road-Map#security--safety)                                         |
| DeFi             | [Explore](https://github.com/OffcierCia/DeFi-Developer-Road-Map#defi)                                                     |
| ENS              | [Explore](https://github.com/OffcierCia/DeFi-Developer-Road-Map#ethereum-name-service)                                    |
| NFT              | [Explore](https://github.com/OffcierCia/DeFi-Developer-Road-Map#non-fungible-token-nft)                                   |
| Stable Coins     | [Explore](https://github.com/OffcierCia/DeFi-Developer-Road-Map#stable-coins)                                             |
| General Info     | [Explore](https://github.com/OffcierCia/DeFi-Developer-Road-Map#ethereum-tools)                                           |
| Side Chains      | [Explore](https://github.com/OffcierCia/DeFi-Developer-Road-Map#side-chains)                                              |
| MEV              | [Explore](https://github.com/OffcierCia/DeFi-Developer-Road-Map#mev---maximal-extractable-value--miner-extractable-value) |
| Tools Collection | [Explore](https://github.com/OffcierCia/DeFi-Developer-Road-Map#tools-collection)                                         |
| ETH 2.0          | [Explore](https://github.com/OffcierCia/DeFi-Developer-Road-Map#ethereum-20)                                              |
| Front End        | [Explore](https://github.com/OffcierCia/DeFi-Developer-Road-Map#front-end)                                                |


# Basics:


- 분산장부 기술의 기본 알아보기 (DLT)
- 비트코인 통신규약 [설명](https://medium.com/coinmonks/bitcoin-white-paper-explained-part-1-4-16cba783146a)
- 타원곡선암호 (Elliptic Curve) [암호학](https://medium.com/coinmonks/learn-how-to-code-elliptic-curve-cryptography-a952dfdc20ab)
- 읽기: [블록체인 설명](https://www.investopedia.com/terms/b/blockchain.asp)
- 보기: [블록체인 - 시각화 데모](https://www.youtube.com/watch?v=_160oMzblY8)

#### 이더리움

- 이더리움의 기본 알아보기
- 이더리움 가상 머신 (EVM): 튜링 완전 지갑, 계정 (EOA), Private/Public Key
- 트렌젝션(transactions), 가스(Gas), 메타마스크(Metamask)
- 이더리움 클라이언트/노드, Geth
- Infura infrastructure

#### 스마트 계약


- 스마트 계약의 기본
- 스마트 계약의 라이프 사이클 알아보기
- 이더리움 상위 레벨 언어 (**솔리디티(Solidity)**, Vyper, LLL, Serpent)
- 컴파일, 테스트, 스마트 계약 배포
- web3.js 또는 web3.py를 이용한 스마트 계약 적용
- [이더리움은 어떻게 작동할까요?](https://medium.com/@preethikasireddy/how-does-ethereum-work-anyway-22d1df506369)
- 읽기: [이 글](https://blog.zeppelin.solutions/the-hitchhikers-guide-to-smart-contracts-in-ethereum-848f08001f05)
- 읽기: [Truffle 공식문서](https://truffleframework.com/docs/) / [Hardhat Documentation](https://hardhat.org/getting-started/)
- 읽기: [Web3 공식문서](https://web3js.readthedocs.io/en/1.0/) / [Ethers Documentation](https://docs.ethers.io/v5/)
- 읽기: [이더리움 마스터](https://github.com/ethereumbook/ethereumbook)
- 읽기: [솔리디티 스마트 계약 라이브러리](https://openzeppelin.org/api/docs/get-started.html)

#### 스마트 계약 표준

- [ERCs](https://eips.ethereum.org/erc) - 이더리움 개선안

#### 토큰

- [ERC-20](https://eips.ethereum.org/EIPS/eip-20) - 유동성 자산에 대한 토큰 계약.
- [ERC-721](https://github.com/ethereum/eips/issues/721) - 비휘발성 자산의 토큰 표준.
- [ERC-918](https://eips.ethereum.org/EIPS/eip-918) - 채굴 가능한 토큰의 표준.

#### 기타

- [ERC-165](https://eips.ethereum.org/EIPS/eip-165) - 스마트 계약가 구현하는 인터페이스를 알아보고 이용하는 표준방법
- [ERC-725](https://eips.ethereum.org/EIPS/eip-725) - 단순 프록시 계정을 위한 표준 인터페이스 
- [ERC-173](https://eips.ethereum.org/EIPS/eip-173) - 계약 소유권을 위한 표준 인터페이스


#### 일반적인 개발 기술들


- Learn [GIT](https://medium.com/pixel-pioneers/the-basics-of-version-control-system-git-explained-by-designing-a-new-car-3fb3a10e9e40)
- 레파지토리를 생성하는 방법 [GitHub](https://github.com/) / [GitLab](https://about.gitlab.com/)
- 당신의 코드를 사람들에게 공개하는 방법: HTTP(S) 통신 규약, request methods (GET, POST, PUT, PATCH, DELETE, OPTIONS)
- 구글을 사용하는 것을 두려워하지 마세요, [구글 검색 더 잘하는법](http://www.powersearchingwithgoogle.com/)
- 터미널에 익숙해지기 ([Linux/Docker](https://medium.com/coinmonks/how-to-become-a-blockchain-developer-59c830e20f15)), 당신의 shell 설정(bash, zsh, fish)
- 알고리즘, 데이터 구조, 블록체인, 이더리움, 견고성에 대한 책을 읽어보세요.
- 이 코스를 해보세요.[이더리움 그리고 솔리디티: 완벽 개발자 가이드](https://www.udemy.com/ethereum-and-solidity-the-complete-developers-guide/)
- 무료 자습서 [솔리디티 배우기](https://github.com/willitscale/learning-solidity)
- [솔리티디를 이용한 스마트 계약 소개](https://www.youtube.com/playlist?list=PLV1JDFUtrXpGvu8QHL9b78WYNSJsYNZsb)

#### 이 툴을 사용해보세요:

- [eth-cli](https://github.com/protofire/eth-cli) - CLI tools.
- [REPL](https://github.com/raineorshine/solidity-repl) - 솔리디티 REPL.
- [Remix](https://remix.ethereum.org/) - 온라인 실시간 컴파일러 그리고 런타임.


# dApps

- 사용할 툴에 익숙해지세요.

#### 패키지 매니저

- [npm](https://www.npmjs.com/)
- [yarn](https://yarnpkg.com/lang/en/)
- [pnpm](https://pnpm.js.org/)

#### IDE's

- [Remix IDE](https://remix.ethereum.org/)
- [Ethfiddle](https://ethfiddle.com/)
- [labs.superblock](https://superblocks.com/)
- [Truffle](https://truffleframework.com/)
- [Solidity v0.5.3](https://solidity.readthedocs.io/en/v0.5.3/)
- [Vyper](https://github.com/ethereum/vyper)
- [Atom](https://atom.io/) 
- [Etheratom](https://atom.io/packages/etheratom)
- [Autocomplete Solidity](https://atom.io/packages/autocomplete-solidity)
- [Language Solidity](https://atom.io/packages/language-solidity) 
- [Vim solidity](https://github.com/tomlion/vim-solidity) 
- [YAKINDU Solidity Tools](https://github.com/Yakindu/solidity-ide) 


 #### 실천

- [Zombie Game](https://cryptozombies.io/)을 통해 이더리움 개발 학습
- 예제를 읽고 만들어보세요: [펫 샵 자습서](https://www.trufflesuite.com/tutorial)
- [시간 잠금 지갑: 이더리움 스마트 계약 소개](https://www.toptal.com/ethereum-smart-contract/time-locked-wallet-truffle-tutorial)
- [The Ultimate ENS 그리고 ĐApp 자습서](https://www.toptal.com/ethereum/ethereum-name-service-dapp-tutorial)
- [Ultimate Introduction to Ethereum Ðapp Development](https://www.youtube.com/playlist?list=PLV1JDFUtrXpFh85G-Ddyy2kLSafaB9biQ)
- [Ethernaut](https://ethernaut.zeppelin.solutions/) is a Web3/Solidity based wargame for those interested in learning ethereum
- [이더리움 그리고 솔리디티: 완벽 개발자 가이드](https://www.udemy.com/ethereum-and-solidity-the-complete-developers-guide/)
- [Consensys 모범 사례](https://consensys.github.io/smart-contract-best-practices/) - 이 문서는 중간에 솔리디티 프로그래머의 보안 사항에 대한 기본 지식을 제공하며 ConsenSys Diligence와 더 넓은 이더리움 커뮤니티로 유지합니다.
- [솔리디티 패턴](https://github.com/fravoll/solidity-patterns) - 패턴과 모범 사례 모음입니다.

# ZK-SNARKs

#### 일반적인 정보

- [ZoKrates](https://github.com/Zokrates/ZoKrates) - 이더리움에서 zkSNARKS을 위한 도구상자
- [The AZTEC Protocol](https://github.com/AztecProtocol/AZTEC) - 이더리움 네트워크에서 거래 및 구현은 메인넷에서 진행됩니다.
- [Nightfall](https://github.com/EYBlockchain/nightfall) - ERC-20 / ERC-721 개인 토큰 - 오픈 소스툴 & 마이크로 서비스 만들기
- 프록시 재암호화 (PRE)
- [NuCypher Network](https://github.com/nucypher/nucypher) - 분산된 시스템에서 개인 정보 보호를 강화하기 위한 프록시 재암호화 네트워크
- [pyUmbral](https://github.com/nucypher/pyumbral) - 임계값 프록시 재암호화 라이브러리
- 완전 동형 암호화 (FHE)
- [NuFHE](https://github.com/nucypher/nufhe) - GPU 가속화 FHE 라이브러리

#### ZK-STARKs
- [StarkWare](https://github.com/starkware-industries) 그리고 [StarkWare Resources](https://github.com/starkware-libs) - StarkEx 확장성 엔진이 상태 전환을 체인에 저장

# 프레임워크

#### Truffle Suit 

- [Truffle](https://truffleframework.com/truffle)
- [Ganache](https://truffleframework.com/ganache)
- [Drizzle](https://truffleframework.com/drizzle)


#### ZeppelinOS

- [Getting Started](https://docs.zeppelinos.org/docs/start.html)

#### Labs.Superblock

- [Labs.superblocks](https://lab.superblocks.com/)
- [dapp Tutorial](https://www.youtube.com/watch?v=LK-kVMzrdno)


#### Infura (이더리움 게이트웨이)

- [Mainnet End Point](https://infura.io/)
- [Ropsten TestNet End Point](https://infura.io/)
- [Kovan TestNet End Point](https://infura.io/)
- [Rinkby TestNet End Point](https://infura.io/)
- [IPFS](https://medium.freecodecamp.org/hands-on-get-started-with-infura-and-ipfs-on-ethereum-b63635142af0)

#### 다른 프레임워크

- [Hardhat](https://hardhat.org/) - 빠르고 유연하며 확장이 가능한 이더리움 개발 환경
- [Brownie](https://github.com/iamdefinitelyahuman/brownie) - Brownie는 이더리움 스마트 계약를 구현, 테스트 및 상호작용하기 위한 파이썬 프레임워크입니다.
- [Embark](https://github.com/embark-framework/embark) - DApp 개발자를 위한 프레임워크
- [Waffle](https://getwaffle.io/) - 고급 스마트 계약 개발 및 테스트를 위한 프레임워크로 작고, 빠르고, 유연하며, 신속합니다.(ether.js 기반)
- [Dapp](https://dapp.tools/dapp/) -  DApp 개발을 위한 프레임 워크, 성공적인 DApple의 후계자
- [Etherlime](https://github.com/LimeChain/etherlime) - ethers.js 기반 Dapp 개발 프레임워크
- [Parasol](https://github.com/Lamarkaz/parasol) - 테스트, INFURA 구축, 자동 계약 문서등을 지원하는 프레임워크로 애자일하며 개발 환경이 유연하고 자유로운 디자인으로 사용자 지정에 제한이 없습니다.
- [0xcert](https://github.com/0xcert/framework/) - 분산 애플리케이션 구축을 위한 자바스크립트 프레임워크
- [OpenZeppelin SDK](https://openzeppelin.com/sdk/) - OpenZeppelin SDK: 스마트 계약을 개발, 컴파일, 업그레이드, 배포 및 상호 작용에 도움이 되는 툴 모음입니다.
- [sbt-ethereum](https://sbt-ethereum.io/) - 지갑 및 ABI 관리, ENS 지원, 고급 스칼라 통합을 비롯한 스마트 계약 상호 작용 개발을 위한 탭 기반 텍스트 콘솔입니다.
- [Cobra](https://github.com/cobraframework/cobra) - 이더리움 스마트 계약, 테스트 및 EVM(Ethereum virtual machine) 구축을 위한 빠르고 유연하며 단순한 개발 환경 프레임워크 입니다.
- [Epirus](https://docs.epirus.io/sdk/) - 스마트 계약을 구축하기 위한 자바 프레임워크


#### 스마트 계약과 상호 작용

- [Web3.js](https://web3js.readthedocs.io/en/1.0/)
- [Web3.py](https://web3py.readthedocs.io/en/stable/)
- [Web3j](https://docs.web3j.io/latest/)

#### 파이썬 이더리움 에코 시스템

- [Article](https://medium.com/@pipermerriam/the-python-ethereum-ecosystem-101bd9ba4de7)

#### 분산 저장 시스템

- [INFO](https://medium.com/bitfwd/what-is-decentralised-storage-ipfs-filecoin-sia-storj-swarm-5509e476995f)
- [IPFS](https://ipfs.io/)
- [SWARM](https://swarm-gateways.net/)
- [Storej](https://storj.io/)
- [Sia](https://sia.tech/)

#### 테스트 블록체인 네트워크

- [Ethnode](https://github.com/vrde/ethnode) - 개발을 위해서 `npm i -g ethnode && ethnode` 같이 쉽게 이더리움 노드를 실행할 수 있습니다. (Geth or Parity)
- [Ganache](https://github.com/trufflesuite/ganache) - 시각적인 UI 및 로그가 포함된 이더리움 블록체인 테스트용 앱입니다.
- [Kaleido](https://kaleido.io/) - Kaleido 를 사용하여 협력 블록체인 네트워크를 구성합니다. PoC와 테스트에 적합합니다.
- [Besu Private Network](https://besu.hyperledger.org/en/stable/Tutorials/Quickstarts/Azure-Private-Network-Quickstart/) - 도커 컨테이너에서 Besu 노드의 전용 네트워크를 실행 할 수 있습니다.
- [Orion](https://github.com/PegaSysEng/orion) - PegaSys에서 개인 트랜잭션을 수행하기 위한 컴포넌트입니다.
- [Artemis](https://github.com/PegaSysEng/artemis) - PegaSys의 이더리움 2.0 비콘 체인 자바 구현체입니다.
- [Cliquebait](https://github.com/f-o-a-m/cliquebait) - 실제 블록체인 네트워크와 매우 유사한 도커 인스턴스를 통해 스마트 계약 애플리케이션의 통합 및 테스트 수용을 간소화 할 수 있습니다.
- [Local Raiden](https://github.com/ConsenSys/Local-Raiden) - 데모 및 테스트를 위해 도커 컨테이너에서 로컬 Raiden 네트워크를 실행 할 수 있습니다.
- [Private networks deployment scripts](https://github.com/ConsenSys/private-networks-deployment-scripts) - 프라이빗 PoA 네트워크를 위한 기본 제공 배포 스크립트입니다.
- [Local Ethereum Network](https://github.com/ConsenSys/local_ethereum_network) - 프라이빗 PoW 네트워크를 위한 기본 제공 배포 스크립트입니다.
- [Ethereum on Azure](https://docs.microsoft.com/en-us/azure/blockchain/templates/ethereum-poa-deployment) - 컨소시엄 이더리움 PoA 네트워크 구축 및 거버넌스를 구축할 수 있습니다.
- [Ethereum on Google Cloud](https://console.cloud.google.com/marketplace/details/click-to-deploy-images/ethereum?filter=category:developer-tools) - PoW기반 이더리움 네트워크를 구축할 수 있습니다.
- [Infura](https://infura.io/) - 이더리움 네트워크에 대한 이더리움 API 엑세스 (Mainnet, Ropsten, Rinkeby, Goerli, Kovan)
- [CloudFlare Distributed Web Gateway](https://cloudflare.com/distributed-web-gateway/) - 자체 노드를 실행하는 대신 Cloudflare를 통해 이더리움 네트워크에 대한 엑세스를 제공합니다.
- [Chainstack](https://chainstack.com/) - 서비스형 이더리움 노드 공유 서비스 (Mainnet, Ropsten, Rinkeby)
- [Alchemy](https://alchemyapi.io/) - 블록체인 개발자 플랫폼, 이더리움 API, 노드서비스 (Mainnet, Ropsten, Rinkeby, Goerli, Kovan)
- [ZMOK](https://zmok.io/) - JSON-RPC 이더리움 API (Mainnet, Rinkeby, Front-running Mainnet)

#### 테스트 Ether Faucets

- [Rinkeby faucet](https://faucet.rinkeby.io/)
- [Kovan faucet](https://github.com/kovan-testnet/faucet)
- [Ropsten faucet (MetaMask)](https://faucet.metamask.io/)
- [Goerli faucet](https://goerli-faucet.slock.it/)
- [Universal faucet](https://faucets.blockxlabs.com/)
- [Nethereum.Faucet](https://github.com/Nethereum/Nethereum.Faucet) - A C#/.NET faucet


# 프론트 엔드

#### UI 컴포넌트

- 리액트를 [공식 사이트](https://reactjs.org/tutorial/tutorial.html) 또는 [코스](https://egghead.io/courses/the-beginner-s-guide-to-react)를 배울 수 있습니다.
- [리액트 로드맵](https://github.com/adam-golab/react-developer-roadmap)
- [aragonUI](https://ui.aragon.org) - Dapp 컴포넌트를 포함한 리액트 라이브러리 
- [components.bounties.network](https://components.bounties.network) - Dapp 컴포넌트를 포함한 리액트 라이브러리 
- [ui.decentraland.org](https://github.com/decentraland/ui) - Dapp 컴포넌트를 포함한 리액트 라이브러리 
- [dapparatus](https://github.com/austintgriffith/dapparatus) - 재사용성이 높은 리액트 Dapp 컴포넌트
- [Metamask ui](https://github.com/MetaMask/metamask-extension/tree/develop/ui/app/components) - 메타마스크 리액트 컴포넌트
- [DappHybrid](https://github.com/Nethereum/Nethereum.DappHybrid) - 웹 기반 분산 애플리케이션을 위한 교차 플랫폼 하이브리드 호스팅 매커니즘
- [Nethereum.UI.Desktop](https://github.com/Nethereum/Nethereum.UI.Desktop) - 교차 플랫폼 데스크톱 지갑 샘플
- [eth-button](https://eth-button.github.io/eth-button/) - 미니멀리스트 기부 버튼
- [Rimble Design System](https://rimble.consensys.design/) - 분산형 애플리케이션을 위한 조정 가능한 컴포넌트 및 설계 표준.
- [3Box Plugins](https://docs.3box.io/build/plugins) - 소셜 기능을 위한 리액트 컴포넌트. 의견, 프로필 그리고 메시지를 포함합니다.


# 추가 읽을거리

#### 영감을 받을 만한 글:

- [이더리움 Dapp 개발자 로드맵](https://github.com/thecryptoshed/eth-dapp-developer-roadmap)
- [DeFi Defence DAO Tools](https://github.com/defi-defense-dao/defi-risk-tools-list#developer-tools) 
- [블록체인 학습 경로](https://github.com/protofire/blockchain-learning-path) 
- [ADF](https://github.com/ong/awesome-decentralized-finance) 
- [DeFi Toolkit](https://github.com/gweicz/defi-toolkit)
- [BlockTools](https://github.com/nujabes403/blockchains-tools)
- [SAW List](https://simpleaswater.com/defi/#analytics)
- [Public APIs](https://github.com/public-apis/public-apis#cryptocurrency)
- [BTC List](https://github.com/igorbarinov/awesome-bitcoin)
- [ConsenSys](https://github.com/ConsenSys/ethereum-developer-tools-list)
- [EVM Tools](https://github.com/CoinCulture/evm-tools)
- [Solidity Pro](https://github.com/bkrem/awesome-solidity)
- [Zhihu Research Base](https://zhuanlan.zhihu.com/p/265374061)
- [OpenZeppelin - Contracts / Test Helpers + More ](https://github.com/OpenZeppelin)
- [멋진 이더리움 리소스 목록](https://medium.com/quiknode/awesome-ethereum-resource-lists-dd28a9c17fc1)
- [포괄적인 이더리움 개발자 리소스 목록](https://github.com/ConsenSys/ethereum-developer-tools-list/blob/master/README.md)
- [스마트 계약 배우기](https://github.com/arbazkiraak/SmartContractLearning)
- [멋진 암호화폐 사회](https://github.com/jpantunes/awesome-cryptoeconomics)


#### 보안과 안전:

- [ The Eye of Horus: Spotting and Analyzing Attacks on Ethereum Smart Contracts](https://arxiv.org/pdf/2101.06204.pdf) -Investigation shows that the number of attacks did not necessarily decrease over the past few years, but for some vulnerabilities remained constant.

- [Analysis of Bitcoin Vulnerability to Bribery Attacks Launched Through Large Transactions](https://arxiv.org/pdf/2105.07501.pdf) -  In this paper, authors design a novel bribery attack and show that this guarantee can be hugely undermined.

- [Vulnerability of Blockchain Technologies to Quantum Attacks](https://arxiv.org/pdf/2105.01815.pdf) - Here authors analyze the major blockchain-based cryptocurrencies deployed today -- including Bitcoin, Ethereum, Litecoin and ZCash, and determine risk exposure to quantum attacks. 

- [BLOCKEYE](https://arxiv.org/pdf/2103.02873.pdf) - Hunting For DeFi Attacks on Blockchain. In this paper, authors proposed BLOCKEYE, a real-time attack detection system for DeFi projects on the Ethereum blockchain. 

- [Topological Anomaly Detection in Dynamic Multilayer Blockchain Networks](https://arxiv.org/pdf/2106.01806.pdf) - Authors introduce a new topological perspective to structural anomaly detection in dynamic multilayer networks.

- [Verification of the Incremental Merkle Tree Algorithm with Dafny](https://arxiv.org/pdf/2105.06009.pdf) - Authors present our new and original correctness proof of the algorithm along with the Dafny machine-checkable version.

- [GoHammer Blockchain Performance Test Tool](https://arxiv.org/pdf/2105.00847.pdf) - This tool will help in developing more efficient decentralized systems and will affect decreasing the costs of developing decentralized application projects.

- [EtherClue: Digital investigation of attacks on Ethereum smart contracts ](https://arxiv.org/pdf/2104.05293.pdf) - In this work, authors study the problem of post-factum investigation of Ethereum attacks using Indicators of Compromise specially crafted for use in the blockchain.

- [Requirement Analyses and Evaluations of Blockchain Platforms per Possible Use Cases](https://arxiv.org/pdf/2103.03209.pdf) - This document provides a generic model of understanding blockchain and its applications.

- [A Note on Privacy in Constant Function Market Makers](https://arxiv.org/pdf/2103.01193.pdf) -  In this note, authors show that privacy is impossible with the usual implementations of CFMMs under most reasonable models of an adversary and provide some mitigating strategies.

- [A Survey of Security Vulnerabilities in Ethereum Smart Contracts](https://arxiv.org/pdf/2105.06974.pdf) -  This paper explains eight vulnerabilities that are specific to the application level of BT by analyzing the exploitation case scenarios of these vulnerabilities.

- [An approach to detect Denial of Service Vulnerability in Ethereum Smart Contracts](https://arxiv.org/pdf/2106.01340.pdf) -  In this paper, authors propose a framework that combines static and dynamic analysis to detect DoS due to an unexpected revert in ETH Smart Contracts.

- [AGSolT: a Tool for Automated Test-Case Generation for Solidity Smart Contracts](https://arxiv.org/pdf/2102.08864.pdf) - Authors found that AGSolT is capable of achieving high branch overage with both approaches and even discovered some errors in some of the most popular Solidity smart contracts on Github.

- [Temporal-Amount Snapshot MultiGraph for Ethereum Transaction Tracking](https://arxiv.org/pdf/2102.08013.pdf) - Authors propose TASMG to model Ethereum transaction records as a temporal-amount network and then present TAW to effectively embed accounts via their transaction records, which integrates temporal and amount information of the proposed network.

- [Demystifying Cryptocurrency Mining Attacks: A Semi-supervised Learning Approach Based on Digital Forensics and Dynamic Network Characteristics](https://arxiv.org/pdf/2102.10634.pdf) - This paper addresses the detection of crypto mining attacks in a generic network environment using dynamic network characteristics. 

- [FASTEN: Fair and Secure Distributed Voting Using Smart Contracts](https://arxiv.org/pdf/2102.10594.pdf) - Authors prove that the probability of privacy breaches is negligibly small. Further, cost analysis of executing FASTEN over Ethereum is comparable to most of the existing cost of elections.

- [Interdependencies between Mining Costs, Mining Rewards and Blockchain Security](https://arxiv.org/pdf/2102.08107.pdf) - This paper studies to what extent the cost of operating a proof-of-work blockchain is intrinsically linked to the cost of preventing attacks, and to what extent the underlying digital ledger security budgets are correlated with the cryptocurrency market outcomes

- [HyperSec: Visual Analytics for blockchain security monitoring](https://arxiv.org/pdf/2103.14414.pdf) - HyperSec, a visual analytics monitoring tool that provides relevant information at a glance to detect ongoing attacks on Hyperledger Fabric. 

- [Reentrancy Vulnerability Identification in Ethereum Smart Contracts](https://arxiv.org/pdf/2105.02881.pdf) - In this paper, authors present a framework that combines static and dynamic analysis to detect Reentrancy vulnerabilities in Ethereum smart contracts.

- [A General Framework for the Security Analysis of Blockchain Protocols](https://arxiv.org/pdf/2009.09480v2.pdf) - This paper presents a parsimonious abstraction sufficient for capturing and comparing properties of many well-known permissionless blockchain protocols.

- [Coinbugs: Enumerating Common Blockchain Implementation-Level Vulnerabilities](https://arxiv.org/pdf/2104.06540.pdf) -  The paper is aimed at security testers aiming to start out in blockchain security reviews and blockchain developers as a reference on common pitfalls.

- [Vulnerabilities and Open Issues of Smart Contracts: A Systematic Mapping](https://arxiv.org/pdf/2104.12295.pdf) - This paper conducted a systematic literature mapping identifying initiatives and tools to analyze SCs and how to deal with the identified vulnerabilities.

- [SuMo: A Mutation Testing Strategy for Solidity Smart Contracts](https://arxiv.org/pdf/2105.03626.pdf) - Authors report a first evaluation of SuMo on open-source projects for which test suites were available. The results authors got are encouraging, and they suggest that SuMo can effectively help developers to deliver more reliable smart contracts.

- [(In)Stability for the Blockchain: Deleveraging Spirals and Stablecoin Attacks](https://arxiv.org/pdf/1906.02152.pdf) - The possibility of deleveraging spirals was first predicted in the initial release of this paper in 2019 and later observed in the Black Thursday crisis in Dai in 2020.

- [An Anonymous Trust-Marking Scheme on Blockchain Systems](https://arxiv.org/pdf/2010.00206.pdf) - In this paper, authors propose an anonymous trust-marking scheme on blockchain systems that is universally applicable to any cryptocurrency.

- [A Framework and DataSet for Bugs in Ethereum Smart Contracts](https://arxiv.org/pdf/2009.02066.pdf) -  In this paper, to fill the gap, authors first collect as many smart contract bugs as possible from multiple sources and divide these bugs into 9 categories by extending the IEEE Standard Classification for Software Anomalies.

- [A Secure Multi-chains Consensus Scheme Against Diverse Miners Behaviors Attacks in Blockchain Networks.](https://arxiv.org/pdf/2106.02383.pdf) - Experimental results show that PoDT is secure against DMB attacks and more effective than traditional consensus schemes in multi-chains environments.

- [A Survey on Consortium Blockchain Consensus Mechanisms](https://arxiv.org/pdf/2102.12058.pdf) - This paper highilights several state-of-the art solutions in consensus algorithms for enterprise blockchain. 

- [Extracting Smart Contracts Tested and Verified in Coq](https://arxiv.org/pdf/2012.09138.pdf) - Authors implement extraction of Coq programs to functional languages based on MetaCoq's certified erasure. 

- [Trustless, privacy-preserving blockchain bridges](https://arxiv.org/pdf/2102.04660.pdf) - In this paper, authors present a protocol for facilitating trust-less cross-chain cryptocurrency transfers that preserve privacy of bridge withdrawals.

- [Security checklists for Ethereum smart contract development: patterns and best practices](https://arxiv.org/pdf/2008.04761.pdf) - Authors cover the phases of design, coding, and testing and deployment of the software lifecycle.

- [Dynamic Vulnerability Detection on Smart Contracts Using Machine Learning](https://arxiv.org/pdf/2102.07420.pdf) - In this work authors propose Dynamit, a monitoring framework to detect reentrancy vulnerabilities in Ethereum smart contracts. 

- [Targeting the Weakest Link: Social Engineering Attacks in Ethereum Smart Contracts](https://arxiv.org/pdf/2105.00132.pdf) - In this work, authors explore the possibility and existence of new social engineering attacks beyond smart contract honeypots.

- [OptSmart: A Space Efficient Optimistic Concurrent Execution of Smart Contracts](https://arxiv.org/pdf/2102.04875.pdf) - In this paper, authors develop a concurrent miner that proposes a block by executing the AUs concurrently using optimistic Software Transactional Memory systems (STMs).

- [DEFECTCHECKER: Automated Smart Contract Defect Detection by Analyzing EVM Bytecode](https://arxiv.org/pdf/2009.02663.pdf) - Experimental results show that DefectChecker performs much better than these tools in terms of both speed and accuracy. 

- [SmartBugs: A Framework to Analyze Solidity Smart Contracts](https://arxiv.org/pdf/2007.04771.pdf) - Authors show how it enables easy integration and comparison of analysis tools by presenting a new extension to the tool SmartCheck that improves substantially the detection of vulnerabilities related to the DASP10 categories Bad Randomness, Time Manipulation, and Access Control (identified vulnerabilities increased from 11% to 24%).

- [Profiling Gas Leaks in Solidity Smart Contracts](https://arxiv.org/pdf/2008.05449.pdf) -  In this paper, authors identify a set of 19 Solidity code smells affecting the deployment and transaction costs of a smart contract, and assess the relevance of such smells through a survey involving 34 participants. 

- [Securing Parallel-chain Protocols under Variable Mining Power](https://arxiv.org/pdf/2105.02927.pdf) -  In this paper, authors consider the design of provably secure parallel-chain protocols which can adapt to such mining power variations. 

- [Ethereum SmartContract Vulnerability Detection using Deep Neural Network and Transfer Learning](https://arxiv.org/pdf/2103.12607.pdf) - ESCORT framework enables transfer learning on new vulnerability types with minimal modification of the DNN model architecture and re-training overhead.

- [SCSGuard: Deep Scam Detection for Ethereum Smart Contracts](https://arxiv.org/pdf/2105.10426.pdf) - Experimental results manifest that SCSGuard achieves high accuracy (0.94), precision (0.96\%) and recall (0.98) for both Ponzi and Honeypot scams, and new Phishing smart contracts.

- [Securing Cyber-Physical Systems Through Blockchain-Based Digital Twins and Threat Intelligence](https://arxiv.org/pdf/2105.08886.pdf) - This article focuses on securing CPSs by integrating Artificial Intelligence (AI) and blockchain for intelligent and trusted DTs. 


#### DeFI


- [Formal Analysis of Composable DeFi Protocols ](https://arxiv.org/pdf/2103.00540.pdf) - In this paper, authors propose a formal process-algebraic technique that models DeFi protocols in a compositional manner to allow for efficient property verification.

- [Transaction Fee Mechanism Design](https://arxiv.org/pdf/2106.01340.pdf) - Authors explain the behavior of fees in blockchains.

- [DeFi-ning DeFi: Challenges & Pathway](https://arxiv.org/pdf/2101.05589.pdf) - Good Retrospective into the beginning of decentralized finance.

- [A theory of Automated Market Makers in DeFi](https://arxiv.org/pdf/2102.11350.pdf) -  Authors exploit our theory to formally prove a set of fundamental properties of AMMs, characterizing both structural and economic aspects. 

- [From banks to DeFi: the evolution of the lending market](https://arxiv.org/pdf/2104.00970.pdf) -  Authors discuss the persisting reliance of DeFi lending on the traditional financial system, and conclude with the outlook of the lending market in the IOV era.

- [On the Just-In-Time Discovery of Profit-Generating Transactions in DeFi Protocols](https://arxiv.org/pdf/2103.02228.pdf) -In this paper, authors investigate two methods that allow them to automatically create profitable DeFi trades.

- [Maximizing Extractable Value from Automated Market Makers](https://arxiv.org/pdf/2106.01870.pdf) -  In this paper authors formally characterize rational miners as players which follow an optimal strategy in the mining game. 

- [The Decentralized Financial Crisis](https://arxiv.org/pdf/2002.08099.pdf) -  In this paper authors explore how design weaknesses and price fluctuations in DeFi protocols could lead to a DeFi crisis.

- [Liquidations: DeFi on a Knife-edge](https://arxiv.org/pdf/2009.13235v4.pdf)- In order to protect protocols from suffering losses, undercollateralized positions can be liquidated. In this paper, authors present empirical analysis of liquidations on protocols for loanable funds (PLFs).

- [Measuring Asset Composability as a Proxy for DeFi Integration](https://arxiv.org/pdf/2102.04227.pdf) -  Authors seek to understand the degree to which this practice may contribute to financial integration on Ethereum by examining transactions in 'composed' derivatives for the assets DAI, USDC, USDT, ETH and tokenized BTC for the full set of 344.8 million Ethereum transactions computed in 2020. 

- [Dynamic Curves for Decentralized Autonomous Cryptocurrency Exchanges](https://arxiv.org/pdf/2101.02778.pdf) -  Authors propose in this work a new approach to constructing the AMM by proposing the idea of dynamic curves.

- [High-Frequency Trading on Decentralized On-Chain Exchanges](https://arxiv.org/pdf/2009.14021.pdf) - In this work authors formalize, analytically exposit and empirically evaluate an augmented variant of front-running: sandwich attacks, which involve front- and back-running victim TXs.

- [Flashot](https://arxiv.org/pdf/2102.00626.pdf) - A Snapshot of Flash Loan Attack on DeFi Ecosystem.

- [DeFiRanger](https://arxiv.org/pdf/2104.15068.pdf) -  Detecting Price Manipulation Attacks on DeFi Applications.

- [Attacking the DeFi Ecosystem with Flash Loans for Fun and Profit](https://arxiv.org/pdf/2003.03810.pdf) - Flash Loans. DeFi. Classic.

- [SoK: Decentralized Finance (DeFi) ](https://arxiv.org/pdf/2101.08778.pdf) - In this Systematization of Knowledge (SoK), authors delineate the DeFi ecosystem along its principal axes. SCSGuard: Deep Scam Detection for Ethereum Smart Contracts

- [Empirical Evidence from four Governance Token Distributions](https://arxiv.org/pdf/2102.10096.pdf) -  This paper provides a framework to quantify decentralization of governance power among blockchain applications.

- [The Adoption of Blockchain-based Decentralized Exchanges](https://arxiv.org/pdf/2103.08842.pdf) -  Authors show that liquidity providers lose token value if exchange rates are volatile due to the order execution mechanism of the blockchain-based exchange.

- [An analysis of Uniswap markets](https://arxiv.org/pdf/1911.03380.pdf) -One of the best studies on Uniswap DEX activity, authors started researching in 2019 and recently released fresh 2021 analysis.

- [Finance 4.0: Design principles for a value-sensitive cryptoecnomic system to address sustainability](https://arxiv.org/pdf/2105.11955.pdf) - Authors provide new insights on designing crypto systems.

- [Behavior of Liquidity Providers in Decentralized Exchanges](https://arxiv.org/pdf/2105.13822.pdf) - Authors aim to understand how liquidity providers react to market information and how they benefit from providing liquidity in DEX.

- [Cyclic Arbitrage in Decentralized Exchange Markets](https://arxiv.org/pdf/2105.02784.pdf) - Good Read. This paper suggests that with the smart contract technology and the replicated state machine setting of Ethereum, arbitrage strategies are easier implemented in DEXes than in CEX.

- [SoK: Oracles from the Ground Truth to Market Manipulation](https://arxiv.org/pdf/2106.00667.pdf) - In this SoK, authors systemize the design alternatives for oracles, showcase attacks, and discuss attack mitigation strategies.

- [Composing Networks of Automated Market Makers](https://arxiv.org/pdf/2106.00083.pdf) - This paper proposes a mathematical model for AMM composition.


#### Ethereum Name Service

- [Ethereum Name Service: the Good, the Bad, and the Ugly](https://arxiv.org/pdf/2104.05185.pdf) - Yet, no existing work has studied this emerging system, the security issues and misbehaviors in ENS. Authors present the first study of ENS by analyzing millions of event logs related to ENS.


#### Non-Fungible Token (NFT):

- [Mapping the NFT revolution](https://arxiv.org/pdf/2106.00647.pdf) - Market trends, trade networks and visual features.

- [Fairness in ERC token markets](https://arxiv.org/pdf/2102.03721.pdf) - A Case Study of CryptoKitties.

- [Non-Fungible Token: Overview, Evaluation, Opportunities and Challenges](https://arxiv.org/pdf/2105.07447.pdf) - In this technical report, authors explore the NFT ecosystems in several aspects.

- [Cryptoart](http://cryptoart.io/) - Top artists and artworks.

- [CryptoArtPulse](https://cryptoartpulse.com/) - Live View.

- [PumpMyGas](https://pumpmygas.xyz/) - Live estimates of gas fees on all major NFT marketplaces.

- [NonFungible Tracker](https://nonfungible.com/) - NFT tracker.

- [NFTS TOP]( https://cryptoslam.io) - NFT Ranking.


#### Stable-Coins:


- [Stablecoins 2.0](https://arxiv.org/pdf/2006.12388.pdf) - Authors seek to provide a sound foundation for stablecoin theory, with a risk-based functional characterization of the economic structure of stablecoins.

- [Reducing the Volatility of Cryptocurrencies — A Survey of Stablecoins](https://arxiv.org/pdf/2103.01340.pdf) -  Authors discuss how stablecoins help reduce the volatility of cryptocurrencies by surveying different types of stablecoins and their stability mechanisms.

- [Understand Volatility of Algorithmic Stablecoin: Modeling, Verification and Empirical Analysis](https://arxiv.org/pdf/2101.08423.pdf) - Authors performed a systematic empirical analysis on real transaction activities of the Basis Cash stablecoin to relate theoretical possibilities to market observations. 

- [T-Cash: Transferable Fiat Backed Coins](https://arxiv.org/pdf/2105.04485.pdf) -  In this paper authors propose a transferable electronic cash scheme using blockchain technology which allows users to continuously reuse coins within the system.


#### General information:


- [A Big Data Analysis of the Ethereum Network: from Blockchain to Google Trends](https://arxiv.org/pdf/2104.01764.pdf) - An analysis of the crypto prices and search trends suggests the existence of big players (and not the regular users), manipulating the market after a drop in prices.

- [A DLT-based Smart Contract Architecture for Atomic and Scalable Trading](https://arxiv.org/pdf/2105.02937.pdf) -  In this paper, authors propose an atomic, scalable and privacy-preserving protocol that enables secure and dynamic updates. Then develop a smart contract-based Credit-Note System (CNS) that allows participants to lock funds before a state channel initialisation, which enhances flexibility and efficiency.

- [Exploring Etherum Data Stores: A Cost and Performance Comparison ](https://arxiv.org/pdf/2105.10520.pdf) -In this work, authors examine a comprehensive set of data management approaches for ETH apps and assess the associated cost in gas as well as the retrieval performance.

- [A Systematic Literature Review on Blockchain Governance](https://arxiv.org/pdf/2105.05460.pdf) - This study comprehensively investigates blockchain governance via 5W1H questions.

- [A general framework for blockchain analytics](https://arxiv.org/pdf/1707.01021.pdf) - Authors propose a general-purpose framework, supporting data analytics on Bitcoin Ethereum — it allows to integrate block data with data from other sources, and to organise them in a database.

- [AMR:Autonomous Coin Mixer with Privacy Preserving Reward Distribution](https://arxiv.org/pdf/2010.01056.pdf) - In this work, authors propose the first censorship resilient mixer, which can reward its users in a privacy-preserving manner for participating in the system.

- [Technology Review of Blockchain Data Privacy Solutions](https://arxiv.org/pdf/2105.01316.pdf)- This report aims to review existing enterprise blockchain technologies: EOSIO powered systems, Hyperledger Fabric and Besu, Consensus Quorum, R3 Corda and Ernst and Young’s Nightfall.

- [Blockchain Systems, Technologies and Applications: A Methodology Perspective](https://arxiv.org/pdf/2105.03572.pdf) - First, this article introduces how blockchain works, the research activity and challenge, and illustrates the roadmap involving the classic methodology with typical blockchain use cases and topics. Second, in blockchain system, how to adopt stochastic process, game theory, optimization, machine learning and cryptography to study blockchain running process and design blockchain protocol/algorithm are discussed in details.

- [Ethna: Analyzing the Underlying Peer-to-Peer Network of the Ethereum Blockchain](https://arxiv.org/pdf/2010.01373.pdf) - Ethna implements a novel method that accurately measures the degrees of Ethereum nodes.

- [Community Detection in Blockchain Social Networks](https://arxiv.org/pdf/2101.06406.pdf) -  A novel community detection algorithm which is designed for low-rank signals on graph can help find users’ communities based on user-token subscription.

- [Block Access Control in Wireless Blockchain Network: Design, Modeling and Analysis](https://arxiv.org/pdf/2104.13144.pdf) -  The results show that BAC approaches can help the network to achieve a high transaction throughput while improving block utilization and saving computational power. Meanwhile, the trade-off between transaction throughput and block utilization is demonstrated, which can act as a guidance for practical deployment of blockchain.

- [Towards External Calls for Blockchain and Distributed Ledger Technology](https://arxiv.org/pdf/2105.10399.pdf) - In this paper authors show that this belief is preconceived by demonstrating a method that enables blockchain and distributed ledger technologies to perform calls to external systems initiated from the blockchain/DLT itself.

- [Managing Blockchain Systems and Applications: A Process Model for Blockchain Configurations](https://arxiv.org/pdf/2105.02118.pdf) - Authors demonstrate the applicability of the proposed blockchain configuration process model on four blockchain projects

- [A Note on Optimal Fees for Constant Function Market Makers](https://arxiv.org/pdf/2105.13510.pdf) -  Authors present framework that can be used to compute optimal fees for real world pools using past trade data.

- [Reward Mechanism for Blockchains Using Evolutionary Game Theory](https://arxiv.org/pdf/2104.05849.pdf) - In this paper, authors develop a reward mechanism framework that could apply to many PoS blockchains.

- [Summing Up Smart Transitions](https://arxiv.org/pdf/2105.07663.pdf) - In this paper, authors present a generalization of first-order logic which can express the unbounded sum of balances. 

- [100+ Metrics for Software Startups - A Multi-Vocal Literature Review](https://arxiv.org/pdf/1901.04819.pdf) -  Using data in the form of metrics can help software startups to make the right decisions amidst uncertainty and limited resources. 

- [Blockchain Networks: Data Structures of Bitcoin , Monero, Zcash, Ethereum, Ripple and IOTA](https://arxiv.org/pdf/2103.08712.pdf) - Authors discuss how blockchain data can be abstracted as various types of networks, and how network abstractions used to reap insights into the structure.

- [Decentralized Finance: On Blockchain- and Smart Contract-Based Financial Markets](https://research.stlouisfed.org/publications/review/2021/02/05/decentralized-finance-on-blockchain-and-smart-contract-based-financial-markets) - Written by Fabian Schar, gives an overview of blockchain based markets with technical details but in a digestable format; great paper for new comers to the space.

#### Side-Chains

- [POA Network](https://www.poa.network/)
- [POA Bridge](https://bridge.poa.net/)
- [POA Bridge UI](https://github.com/poanetwork/bridge-ui)
- [POA Bridge Contracts](https://github.com/poanetwork/poa-bridge-contracts)
- [Loom Network](https://github.com/loomnetwork)
- [Matic Network](https://docs.matic.network/)


#### EIP - 1559

- [Dynamical Analysis of the EIP-1559 Ethereum Fee Market](https://arxiv.org/pdf/2102.10567.pdf)- Authors perform a thorough analysis of the resulting fee market dynamic mechanism via a combination of tools from game theory and dynamical systems.

- [Stochastic Properties of EIP1559 Basefees](https://arxiv.org/pdf/2105.03521.pdf) - Authors explain the new pricing mechanism for the Ethereum developed to bring stability to fluctuating gas prices.

- [Transaction Fee Mechanism Design for the Ethereum Blockchain: An Economic Analysis of EIP-1559](https://arxiv.org/pdf/2012.00854.pdf) - This report assesses the game-theoretic strengths and weaknesses of the proposal and explores some alternative designs.


#### Ethereum 2.0


- [Beaconcha](https://beaconcha.in/)
- [Beaconscan](https://beaconscan.com/)
- [Ethereum 2.0 Stats](https://eth2stats.io/)
- [Ethereum 2.0 Docs](https://docs.ethhub.io/ethereum-roadmap/ethereum-2.0/eth-2.0-phases/)
- [Ethereum 2.0 Clients](https://docs.ethhub.io/ethereum-roadmap/ethereum-2.0/eth2.0-teams/teams-building-eth2.0/)
- [Ethereum 2.0 Forks](https://eth2-fork-mon.stokes.io/) 


#### MEV - Maximal Extractable Value / Miner Extractable Value:


- [Quantifying Blockchain Extractable Value: How dark is the forest?](https://arxiv.org/pdf/2101.05511v2.pdf) - Authors provide evidence that miners already extract Miner Extractable Value (MEV), which could destabilize the blockchain consensus security, as related work has shown.

- [Flash Boys 2.0: Frontrunning, Transaction Reordering, and Consensus Instability in Decentralized Exchanges](https://arxiv.org/pdf/1904.05234.pdf) - Introduces the concept of MEV, the work highlights the large, complex risks created by transaction-ordering dependencies in smart contracts and the ways in which traditional forms of financial-market exploitation are adapting to and penetrating blockchain economies.

- [Flashbots: MEV in Eth2](https://hackmd.io/@flashbots/mev-in-eth2) - In this post, authors study transaction ordering in eth2 and analyze MEV-enabled staking yields. Then they find that MEV will significantly boost validator rewards but may reinforce inequalities among participants of eth2. Authors also discuss qualitative aspects of MEV in eth2 such as the potential dynamics that will unfold between its largest stakeholders like exchanges and validator pools.

#### Disucssion

- [SmartContractResearch Forum](https://www.smartcontractresearch.org) 


 #### Hack Incident Reporting

- [Rekt News](https://rekt.eth.link/leaderboard) - Anonymous platform for whistleblowers and DeFi detectives to present their information to the community.
- [Blockchain Threat Intelligence](https://blockthreat.substack.com/) - Newsletter covering the latest security news, tools, events, vulnerabilities, and threats in the cryptocurrency landscape. Also [supports this repo.](https://github.com/openblocksec/blocksec-incidents)
- [Blockchain Graveyard](https://magoo.github.io/Blockchain-Graveyard/) - A list of all massive security breaches or thefts involving blockchains.


# Tools Collection


#### Ethereum Tools

- [Ethstats](https://ethstats.io)
- [ETH Forks](https://forkmon.ethdevops.io) 
- [Node Stats](https://ethernodes.org)
- [EVM Networks List](https://chainid.network)
- [BIP39 Derivation](https://iancoleman.io/bip39)
- [Vanity Generator](https://github.com/johguse/profanity) 
- [Web Vanity Generator](https://vanity-eth.tk) 
- [Vanity Eth Generators](https://github.com/search?q=eth+vanity)
- [FindETH](https://findeth.io) 
- [Eth Tx Decoder](https://antoncoding.github.io/eth-tx-decoder)
- [Ethereum input data decoder](https://lab.miguelmota.com/ethereum-input-data-decoder)
- [Ethereum Gas Charts](https://ethereumprice.org/gas)
- [Ethereum TxPool Statistics](https://txpool.zengo.com/) 
- [Gas Prices Dashboard ](https://explore.duneanalytics.com/public/dashboards/qswVMdzbyiiZFdnCDSwx1jfYLOjdaokM4CSGNxsH)
- [The UI from ABI](https://ethcontract.watch)
- [Oracles Club](https://oracles.club)
- [Tx Combo](https://furucombo.app)
- [ETH or ERC-20 Mass-sender](https://disperse.app)
- [BulkSender](https://bulksender.app)
- [ERC20 Meta Token Wrapper](https://github.com/arcadeum/erc20-meta-token) 
- [Cancel Ethereum Transaction](https://github.com/mds1/Cancel-Ethereum-Transactions)
- [Fees WTF Calculator](https://fees.wtf) 
- [Spend Gas Stats](https://txn.finance) 
- [Pools Stats](https://pools.fyi) 
- [Solhint](https://github.com/protofire/solhint) 
- [Solium](https://github.com/duaraghav8/Solium)
- [Sol-tester](https://github.com/androlo/sol-tester) 
- [Solidity-coverage](https://github.com/sc-forks/solidity-coverage) 
- [TypeChain](https://github.com/ethereum-ts/TypeChain) 


#### Libraries

- [dapp-bin](https://github.com/ethereum/dapp-bin) - Ethereum repo providing implementations for many common data structures and utilities in Solidity, Serpent and LLL.
- [Solidity Collections](https://github.com/ethereum/wiki/wiki/Solidity-Collections) - Collections of code snippets and utility libraries.
- [OpenZeppelin](https://openzeppelin.org/) - Framework to build secure smart contracts.

#### Popular Smart Contract Libraries

- [Zeppelin](https://github.com/OpenZeppelin/openzeppelin-contracts) - Contains tested reusable smart contracts like SafeMath and OpenZeppelin SDK [library](https://github.com/OpenZeppelin/openzeppelin-sdk) for smart contract upgradeability
- [cryptofin-solidity](https://github.com/cryptofinlabs/cryptofin-solidity) - A collection of Solidity libraries for building secure and gas-efficient smart contracts on Ethereum.
- [Modular Libraries](https://github.com/Modular-Network/ethereum-libraries) - A group of packages built for use on blockchains utilising the Ethereum Virtual Machine
- [DateTime Library](https://github.com/bokkypoobah/BokkyPooBahsDateTimeLibrary) - A gas-efficient Solidity date and time library
- [Aragon](https://github.com/aragon/aragon) - DAO protocol. Contains [aragonOS smart contract framework](https://github.com/aragon/aragonOS) with focus on upgradeability and governance
- [ARC](https://github.com/daostack/arc) - an operating system for DAOs and the base layer of the DAO stack.
- [0x](https://github.com/0xProject) - DEX protocol
- [Token Libraries with Proofs](https://github.com/sec-bit/tokenlibs-with-proofs) - Contains correctness proofs of token contracts wrt. given specifications and high-level properties
- [Provable API](https://github.com/provable-things/ethereum-api) - Provides contracts for using the Provable service, allowing for off-chain actions, data-fetching, and computation
- [ABDK Libraries for Solidity](https://github.com/abdk-consulting/abdk-libraries-solidity) - Fixed-point (64.64 bit) and IEEE-754 compliant quad precision (128 bit) floating-point math libraries for Solidity

#### Patterns for Smart Contracts

- [Dappsys: Safe, simple, and flexible Ethereum contract building blocks](https://github.com/dapphub/dappsys)
- [MakerDAO](https://github.com/makerdao/maker-otc)
- [The TAO](https://github.com/ryepdx/the-tao)
- [Dapp-a-day 1-10](https://steemit.com/@nikolai)
- [Dapp-a-day 11-25](https://steemit.com/@nexusdev)
- [OpenZeppelin Contracts: An open framework of reusable and secure smart contracts in the Solidity language.](https://github.com/OpenZeppelin/openzeppelin-contracts)
- [Blog about Best Practices with Security Audits](https://blog.openzeppelin.com/)
- [Advanced Workshop with Assembly](https://github.com/androlo/solidity-workshop)
- [Simpler Ethereum Multisig](https://medium.com/@ChrisLundkvist/exploring-simpler-ethereum-multisig-contracts-b71020c19037) - especially section _Benefits_
- [CryptoFin Solidity Auditing Checklist](https://github.com/cryptofinlabs/audit-checklist) - A checklist of common findings, and issues to watch out for when auditing a contract for a mainnet launch.
- [aragonOS: A smart contract framework for building DAOs, Dapps and protocols](https://hack.aragon.org/docs/aragonos-intro.html)
   

#### Upgradeability
- [Blog von Elena Dimitrova, Dev at colony.io](https://blog.colony.io/author/elena/)
- [Library driven development](https://blog.aragon.org/library-driven-development-in-solidity-2bebcaf88736)
- [Advanced Solidity code deployment techniques](https://blog.aragon.org/advanced-solidity-code-deployment-techniques-dc032665f434/)
- [OpenZeppelin on Proxy Libraries](https://blog.openzeppelin.com/proxy-libraries-in-solidity-79fbe4b970fd/)


#### Developer Tools 

- [CryptoFin Solidity Auditing Checklist](https://github.com/cryptofinlabs/audit-checklist) - A checklist of common findings, and issues to watch out for when auditing a contract for a mainnet launch.
- [MythX](https://mythx.io/) - Security verification platform and tools ecosystem for Ethereum developers
- [Mythril](https://github.com/ConsenSys/mythril) - Open-source EVM bytecode security analysis tool
- [Oyente](https://github.com/melonproject/oyente) - Alternative static smart contract security analysis
- [Securify](https://securify.chainsecurity.com/) - Security scanner for Ethereum smart contracts
- [SmartCheck](https://tool.smartdec.net/) - Static smart contract security analyzer
- [Ethersplay](https://github.com/crytic/ethersplay) - EVM disassembler
- [Evmdis](https://github.com/Arachnid/evmdis) - Alternative EVM disassembler
- [Hydra](https://github.com/IC3Hydra/Hydra) - Framework for cryptoeconomic contract security, decentralised security bounties
- [Solgraph](https://github.com/raineorshine/solgraph) - Visualise Solidity control flow for smart contract security analysis
- [Manticore](https://github.com/trailofbits/manticore) - Symbolic execution tool on Smart Contracts and Binaries
- [Slither](https://github.com/crytic/slither) - A Solidity static analysis framework
- [Adelaide](https://github.com/sec-bit/adelaide) - The SECBIT static analysis extension to Solidity compiler
- [solc-verify](https://github.com/SRI-CSL/solidity/) - A modular verifier for Solidity smart contracts
- [Solidity security blog](https://github.com/sigp/solidity-security-blog) - Comprehensive list of known attack vectors and common anti-patterns
- [Awesome Buggy ERC20 Tokens](https://github.com/sec-bit/awesome-buggy-erc20-tokens) - A Collection of Vulnerabilities in ERC20 Smart Contracts With Tokens Affected
- [Free Smart Contract Security Audit](https://callisto.network/smart-contract-audit/) - Free smart contract security audits from Callisto Network
- [Piet](https://piet.slock.it) - A visual Solidity architecture analyzer

#### Frontend Ethereum APIs


- [Web3.js](https://github.com/ethereum/web3.js/) - Javascript Web3
- [Eth.js](https://github.com/ethjs) - Javascript Web3 alternative
- [Ethers.js](https://github.com/ethers-io/ethers.js/) - Javascript Web3 alternative, useful utilities and wallet features
- [light.js](https://github.com/paritytech/js-libs/tree/master/packages/light.js) A high-level reactive JS library optimized for light clients.
- [Web3Wrapper](https://github.com/0xProject/0x-monorepo/tree/development/packages/web3-wrapper) - Typescript Web3 alternative
- [Ethereumjs](https://github.com/ethereumjs/) - A collection of utility functions for Ethereum like [ethereumjs-util](https://github.com/ethereumjs/ethereumjs-util) and [ethereumjs-tx](https://github.com/ethereumjs/ethereumjs-tx)
- [Alchemy-web3.js](https://github.com/alchemyplatform/alchemy-web3) - Javascript Web3 wrapper with automatic retries, access to [Alchemy's enhanced APIs](https://docs.alchemyapi.io/documentation/alchemy-web3/enhanced-web3-api), and robust websocket connections. 
- [flex-contract](https://github.com/merklejerk/flex-contract) and [flex-ether](https://github.com/merklejerk/flex-ether) - Modern, zero-configuration, high-level libraries for interacting with smart contracts and making transactions.
- [ez-ens](https://github.com/merklejerk/ez-ens) - Simple, zero-configuration Ethereum Name Service address resolver.
- [web3x](https://github.com/xf00f/web3x) - A TypeScript port of web3.js. Benefits includes tiny builds and full type safety, including when interacting with contracts.
- [Nethereum](https://github.com/Nethereum/) - Cross-platform Ethereum development framework
- [dfuse](https://github.com/dfuse-io/client-js) - A TypeScript library to use [dfuse Ethereum API](https://dfuse.io)
- [Drizzle](https://github.com/truffle-box/drizzle-box) - Redux library to connect a frontend to a blockchain
- [Tasit SDK](https://github.com/tasitlabs/tasitsdk) - A JavaScript SDK for making native mobile Ethereum dapps using React Native
- [useMetamask](https://github.com/mdtanrikulu/use-metamask) - a custom React Hook to manage Metamask in Ethereum ĐApp projects
- [WalletConnect](https://walletconnect.org/) - Open protocol for connecting Wallets to Dapps
- [Subproviders](https://0x.org/docs/tools/subproviders) - Several useful subproviders to use in conjunction with [Web3-provider-engine](https://github.com/MetaMask/web3-provider-engine) (including a LedgerSubprovider for adding Ledger hardware wallet support to your dApp)
- [ethvtx](https://github.com/ticket721/ethvtx) - ethereum-ready & framework-agnostic redux store configuration. [docs](https://ticket721.github.io/ethvtx/)
- Strictly Typed - Javascript alternatives
- [elm-ethereum](https://github.com/cmditch/elm-ethereum)
- [purescript-web3](https://github.com/f-o-a-m/purescript-web3)
- [ChainAbstractionLayer](https://github.com/liquality/chainabstractionlayer) - Communicate with different blockchains (including Ethereum) using a single interface.
- [Delphereum](https://github.com/svanas/delphereum) - a Delphi interface to the Ethereum blockchain that allows for development of native dApps for Windows, macOS, iOS, and Android.
- [Torus](https://tor.us/) - Open-sourced SDK to build dapps with a seamless onboarding UX
- [Fortmatic](https://fortmatic.com/) - A simple to use SDK to build web3 dApps without extensions or downloads.
- [Portis](https://portis.io/) - A non-custodial wallet with an SDK that enables easy interaction with DApps without installing anything.
- [create-eth-app](https://github.com/paulrberg/create-eth-app) - Create Ethereum-powered front-end apps with one command.
- [Scaffold-ETH](https://github.com/austintgriffith/scaffold-eth) - Beginner friendly forkable github for getting started building smart contracts. 
- [Notify.js](https://blocknative.com/notify) - Deliver real-time notifications to your users. With built-in support for Speed-Ups and Cancels, Blocknative Notify.js helps users transact with confidence. Notify.js is easy to integrate and quick to customize.

#### Backend Ethereum APIs

- [Web3.py](https://github.com/ethereum/web3.py) - Python Web3
- [Web3.php](https://github.com/sc0Vu/web3.php) - PHP Web3
- [Ethereum-php](https://github.com/digitaldonkey/ethereum-php) - PHP Web3
- [Web3j](https://github.com/web3j/web3j) - Java Web3
- [Nethereum](https://nethereum.com/) - .Net Web3
- [Ethereum.rb](https://github.com/EthWorks/ethereum.rb) - Ruby Web3
- [rust-web3](https://github.com/tomusdrw/rust-web3) - Rust Web3
- [ethers-rs](https://github.com/gakonst/ethers-rs/) - Ethers-rs
- [Web3.hs](https://hackage.haskell.org/package/web3) - Haskell Web3
- [KEthereum](https://github.com/komputing/KEthereum) - Kotlin Web3
- [Eventeum](https://github.com/ConsenSys/eventeum) - A bridge between Ethereum smart contract events and backend microservices, written in Java by Kauri
- [Ethereumex](https://github.com/mana-ethereum/ethereumex) - Elixir JSON-RPC client for the Ethereum blockchain
- [Ethereum-jsonrpc-gateway](https://github.com/HydroProtocol/ethereum-jsonrpc-gateway) - A gateway that allows you to run multiple Ethereum nodes for redundancy and load-balancing purposes. Can be ran as an alternative to (or on top of) Infura. Written in Golang. 
- [EthContract](https://github.com/AgileAlpha/eth_contract) - A set of helper methods to help query ETH smart contracts in Elixir
- [Ethereum Contract Service](https://github.com/mesg-foundation/service-ethereum-contract) - A MESG Service to interact with any Ethereum contract based on its address and ABI.
- [Ethereum Service](https://github.com/mesg-foundation/service-ethereum) - A MESG Service to interact with events from Ethereum and interact with it.
- [Marmo](https://marmo.io/) - Python, JS, and Java SDK for simplifying interactions with Ethereum. Uses relayers to offload transaction costs to relayers.
- [Ethereum Logging Framework](https://bitbucket.csiro.au/users/kli039/repos/ethereum-logging-framework/browse) - provides advanced logging capabilities for Ethereum applications and networks including a query language, query processor, and logging code generation

#### Ethereum Clients

- [Besu](https://besu.hyperledger.org/en/latest/) - an open-source Ethereum client developed under the Apache 2.0 license and written in Java. The project is hosted by Hyperledger.
- [Geth](https://geth.ethereum.org/docs/) - Go client
- [Erigon](https://github.com/ledgerwatch/erigon) - a mostly Go implementation of Ethereum client built on the efficiency frontier
- [OpenEthereum](https://github.com/openethereum/openethereum) - Rust client, formerly called Parity. On path to deprecation in favor of Erigon.
- [Aleth](https://github.com/ethereum/aleth) - C++ client
- [Nethermind](https://github.com/NethermindEth/nethermind) - .NET Core client
- [Infura](https://infura.io/) - A managed service providing Ethereum client standards-compliant APIs
- [Trinity](https://trinity.ethereum.org/) - Python client using [py-evm](https://github.com/ethereum/py-evm)
- [Ethereumjs](https://github.com/ethereumjs/ethereumjs-client) - JS client using [ethereumjs-vm](https://github.com/ethereumjs/ethereumjs-vm)
- [Seth](https://github.com/dapphub/dapptools/tree/master/src/seth) - Seth is an Ethereum client tool—like a "MetaMask for the command line"
- [Mustekala](https://github.com/musteka-la/mustekala) - Ethereum Light Client project of Metamask
- [Exthereum](https://github.com/exthereum/blockchain) - Elixir client
- [EWF Parity](https://github.com/energywebfoundation/energyweb-ui) - Energy Web Foundation client for the Tobalaba test network
- [Quorum](https://github.com/jpmorganchase/quorum) - A permissioned implementation of Ethereum supporting data privacy by [JP Morgan](https://jpmorgan.com/quorum)
- [Mana](https://github.com/mana-ethereum/mana) - Ethereum full node implementation written in Elixir.
- [Chainstack](https://chainstack.com/) - A managed service providing shared and dedicated Geth nodes
- [QuikNode](https://quiknode.io/) - Blockchain developer cloud with API access and node-as-a-service.


#### Storage

- [IPFS](https://ipfs.io/) - Decentralised storage and file referencing
- [Mahuta](https://github.com/ConsenSys/Mahuta) - IPFS Storage service with added search capability, formerly IPFS-Store
- [OrbitDB](https://github.com/orbitdb/orbit-db) - Decentralised database on top of IPFS
- [JS IPFS API](https://github.com/ipfs/js-ipfs-http-client) - A client library for the IPFS HTTP API, implemented in JavaScript
- [TEMPORAL](https://github.com/RTradeLtd/Temporal) - Easy to use API into IPFS and other distributed/decentralised storage protocols
- [PINATA](https://pinata.cloud) - The Easiest Way to Use IPFS
- [Swarm](https://swarm-gateways.net/) - Distributed storage platform and content distribution service, a native base layer service of the Ethereum web3 stack
- [Infura](https://infura.io/) - A managed IPFS API Gateway and pinning service
- [3Box Storage](https://docs.3box.io/api/storage) - An api for user controlled, distrubuted storage. Built on top of IPFS and Orbitdb.
- [Aleph.im](https://aleph.im/) - an offchain incentivized peer-to-peer cloud project (database, file storage, computing and DID) compatible with Ethereum and IPFS.

#### Bootstrap/Out-of-Box tools

- [Truffle boxes](https://trufflesuite.com/boxes) - Packaged components for the Ethereum ecosystem
- [Create Eth App](https://github.com/paulrberg/create-eth-app) - Create Ethereum-powered frontend apps with one command
- [Besu Private Network](https://besu.hyperledger.org/en/stable/Tutorials/Quickstarts/Azure-Private-Network-Quickstart/) - Run a private network of Besu nodes in a Docker container
- [Testchains](https://github.com/Nethereum/TestChains) - Pre-configured .NET devchains for fast response (PoA) 
- [Blazor/Blockchain Explorer](https://github.com/Nethereum/NethereumBlazor) - Wasm blockchain explorer (functional sample)
- [Local Raiden](https://github.com/ConsenSys/Local-Raiden) - Run a local Raiden network in docker containers for demo and testing purposes
- [Private networks deployment scripts](https://github.com/ConsenSys/private-networks-deployment-scripts) - Out-of-the-box deployment scripts for private PoA networks
- [Parity Demo-PoA Tutorial](https://wiki.parity.io/Demo-PoA-tutorial.html) - Step-by-Step tutorial for building a PoA test chain with 2 nodes with Parity authority round consensus
- [Local Ethereum Network](https://github.com/ConsenSys/local_ethereum_network) - Out-of-the-box deployment scripts for private PoW networks
- [Kaleido](https://kaleido.io/) - Use Kaleido for spinning up a consortium blockchain network. Great for PoCs and testing
- [Cheshire](https://github.com/endless-nameless-inc/cheshire) - A local sandbox implementation of the CryptoKitties API and smart contracts, available as a Truffle Box
- [aragonCLI](https://github.com/aragon/aragon-cli) - aragonCLI is used to create and develop Aragon apps and organizations.
- [ColonyJS](https://github.com/JoinColony/colonyJS) - JavaScript client that provides an API for interacting with the Colony Network smart contracts.
- [ArcJS](https://github.com/daostack/arc.js) - Library that facilitates javascript application access to the DAOstack Arc ethereum smart contracts.
- [Arkane Connect](https://docs.arkane.network/pages/connect-js.html) - JavaScript client that provides an API for interacting with Arkane Network, a wallet provider for building user-friendly dapps.
- [Onboard.js](https://blocknative.com/onboard) - Blocknative Onboard is the quick and easy way to add multi-wallet support to your project. With built-in modules for more than 20 unique hardware and software wallets, Onboard saves you time and headaches. 
- [web3-react](https://github.com/NoahZinsmeister/web3-react) - React framework for building single-page Ethereum dApps

#### Ethereum ABI (Application Binary Interface) tools

- [ABI decoder](https://github.com/ConsenSys/abi-decoder) - library for decoding data params and events from Ethereum transactions
- [ABI-gen](https://github.com/0xProject/0x-monorepo/tree/development/packages/abi-gen) - Generate Typescript contract wrappers from contract ABI's.
- [Ethereum ABI UI](https://github.com/hiddentao/ethereum-abi-ui) - Auto-generate UI form field definitions and associated validators from an Ethereum contract ABI
- [headlong](https://github.com/esaulpaugh/headlong/) - type-safe Contract ABI and Recursive Length Prefix library in Java
- [EasyDapper](https://www.easydapper.com) - Generate dapps from Truffle artifacts, deploy contracts on public/private networks, offers live customizable public page to interact with contracts.
- [One Click dApp](https://oneclickdapp.com) - Instantly create a dApp at a unique URL using the ABI.
- [Truffle Pig](https://npmjs.com/package/trufflepig) - a development tool that provides a simple HTTP API to find and read from Truffle-generated contract files, for use during local development. Serves fresh contract ABIs over http.
- [Ethereum Contract Service](https://github.com/mesg-foundation/service-ethereum-contract) - A MESG Service to interact with any Ethereum contract based on its address and ABI.
- [Nethereum-CodeGenerator](https://github.com/StefH/Nethereum-CodeGenerator) - A web based generator which creates a Nethereum based C# Interface and Service based on Solidity Smart Contracts.


# Testing Tools

- [Truffle Teams](https://trufflesuite.com/teams) - Zero-Config continuous integration for truffle projects
- [Solidity code coverage](https://github.com/0xProject/0x-monorepo/tree/development/packages/sol-coverage) - Solidity code coverage tool
- [Solidity coverage](https://github.com/sc-forks/solidity-coverage) - Alternative code coverage for Solidity smart-contracts
- [Solidity function profiler](https://github.com/EricR/sol-function-profiler) - Solidity contract function profiler
- [Sol-profiler](https://github.com/Aniket-Engg/sol-profiler) - Alternative and updated Solidity smart contract profiler
- [Espresso](https://github.com/hillstreetlabs/espresso) - Speedy, parallelised, hot-reloading solidity test framework
- [Eth tester](https://github.com/ethereum/eth-tester) - Tool suite for testing Ethereum applications
- [Cliquebait](https://github.com/f-o-a-m/cliquebait) - Simplifies integration and accepting testing of smart contract applications with docker instances that closely resembles a real blockchain network
- [Hevm](https://github.com/dapphub/dapptools/tree/master/src/hevm) - The hevm project is an implementation of the Ethereum virtual machine (EVM) made specifically for unit testing and debugging smart contracts
- [Ethereum graph debugger](https://github.com/fergarrui/ethereum-graph-debugger) - Solidity graphical debugger
- [Tenderly CLI](https://github.com/Tenderly/tenderly-cli) - Speed up your development with human readable stack traces
- [Solhint](https://github.com/protofire/solhint) - Solidity linter that provides security, style guide and best practice rules for smart contract validation
- [Ethlint](https://github.com/duaraghav8/Ethlint) - Linter to identify and fix style & security issues in Solidity, formerly Solium
- [Decode](https://github.com/hacker-DOM/decode) - npm package which parses tx's submitted to a local testrpc node to make them more readable and easier to understand
- [truffle-assertions](https://github.com/rkalis/truffle-assertions) - An npm package with additional assertions and utilities used in testing Solidity smart contracts with truffle. Most importantly, it adds the ability to assert whether specific events have (not) been emitted.
- [Psol](https://github.com/Lamarkaz/psol) - Solidity lexical preprocessor with mustache.js-style syntax, macros, conditional compilation and automatic remote dependency inclusion.
- [solpp](https://github.com/merklejerk/solpp) - Solidity preprocessor and flattener with a comprehensive directive and expression language, high precision math, and many useful helper functions.
- [Decode and Publish](https://flightwallet.github.io/decode-eth-tx/) – Decode and publish raw ethereum tx. Similar to https://live.blockcypher.com/btc-testnet/decodetx/
- [Doppelgänger](https://getdoppelganger.io/) - a library for mocking smart contract dependencies during unit testing.
- [rocketh](https://github.com/wighawag/rocketh) - A simple lib to test ethereum smart contract that allow to use whatever web3 lib and test runner you choose.
- [pytest-cobra](https://github.com/cobraframework/pytest-cobra) - PyTest plugin for testing smart contracts for Ethereum blockchain.


#### Transaction Visualization, Scoring & Tracking:

- [C-Hound](http://c-hound.ai) 
- [BlockPath](http://blockpath.com) 
- [Maltego](http://maltego.com) 
- [GraphSense](http://graphsense.info) 
- [AML Bot](https://amlbot.com) 
- [Bank Verified](https://bitrankverified.com/home) 
- [Orbit](https://github.com/s0md3v/Orbit)
- [Arronax](https://github.com/Cryptonomic/Arronax)
- [Blockscout](https://github.com/blockscout/blockscout)
- [BTC Parser](https://btcparser.com)
- [Txstreet](https://txstreet.com/v/eth)
- [Nansen](https://www.nansen.ai)
- [Bloxy](https://bloxy.info)
- [Solana Explorer](https://solscan.io)
- [Elliptic](https://www.elliptic.co)
- [ANChain AI](https://www.anchain.ai)
- [Cipher Trace](https://ciphertrace.com)
- [Crystal Blockchain](https://crystalblockchain.com/products)
- [Uppsala Security](https://uppsalasecurity.com)
- [Coinfirm](https://www.coinfirm.com)
- [Solidus Labs](https://www.soliduslabs.com)
- [TRM Labs](https://trmlabs.com)
- [Halborn Forensic](https://halborn.com)


## Support Project:


Support is **very** important to me, with it I can spend less time at work and do what I love - educating DeFi & Crypto users :sparkling_heart:

If you want to support my work, you can send me a donation to the address:

**0xB25C5E8fA1E53eEb9bE3421C59F6A66B786ED77A** — ERC20 & ETH

**32kToCep8CiSS1mLAYE763xBbZaeoHtFgi** — BTC

##


(👍 ͡❛ ͜ʖ ͡❛)👍

