# 디파이 개발자 로드맵

**여기서 최고의 디파이 & 블록체인 연구 그리고 도구을 수집하고 의논합니다. - 기여는 환영합니다.**

**작은 수정 사항부터 번역, 문서, 도구 등 자유롭게 풀 요청을 제출해주세요.**

[![Support Project](https://img.shields.io/badge/Support-Project-critical)](https://github.com/OffcierCia/DeFi-Developer-Road-Map#support-project) [![Research Base](https://img.shields.io/badge/Research-Base-lightgrey)](https://github.com/OffcierCia/ultimate-defi-research-base) [![Supported by LEGO](https://img.shields.io/badge/Supported%20by-LEGO-%2300A3FF)](https://www.notion.so/LEGO-Lido-Ecosystem-Grants-Organisation-d7f0bf0182d44348b6173639d2e8363d) [![Mail](https://img.shields.io/badge/Mail-offcierciapr%40protonmail.com-brightgreen)](mailto:offcierciapr@protonmail.com)

<details>
<summary>번역</summary>
<br>
 <a href="translations/README_guj.md">구자라트어(Gujarati)</a>
 <a href="translations/README_ko.md">한국어(Korean)</a>
</details>

## 로드맵

![Roadmap](../DeFiDevRroadMap_-4-Page-1.svg)

# Navigation

|      Topic       | Instant Link                                                                                                              |
| :--------------: | ------------------------------------------------------------------------------------------------------------------------- |
|       기본       | [Explore](https://github.com/OffcierCia/DeFi-Developer-Road-Map#basics)                                                   |
|      dApps       | [Explore](https://github.com/OffcierCia/DeFi-Developer-Road-Map#dapps)                                                    |
|    프레임워크    | [Explore](https://github.com/OffcierCia/DeFi-Developer-Road-Map#frameworks)                                               |
|   영지식 증명    | [Explore](https://github.com/OffcierCia/DeFi-Developer-Road-Map#zk-snarks)                                                |
| Further Readings | [Explore](https://github.com/OffcierCia/DeFi-Developer-Road-Map#further-readings)                                         |
|       보안       | [Explore](https://github.com/OffcierCia/DeFi-Developer-Road-Map#security--safety)                                         |
|      디파이      | [Explore](https://github.com/OffcierCia/DeFi-Developer-Road-Map#defi)                                                     |
|       ENS        | [Explore](https://github.com/OffcierCia/DeFi-Developer-Road-Map#ethereum-name-service)                                    |
|       NFT        | [Explore](https://github.com/OffcierCia/DeFi-Developer-Road-Map#non-fungible-token-nft)                                   |
|  스테이블 코인   | [Explore](https://github.com/OffcierCia/DeFi-Developer-Road-Map#stable-coins)                                             |
|  일반적인 정보   | [Explore](https://github.com/OffcierCia/DeFi-Developer-Road-Map#ethereum-tools)                                           |
|   사이드 체인    | [Explore](https://github.com/OffcierCia/DeFi-Developer-Road-Map#side-chains)                                              |
|       MEV        | [Explore](https://github.com/OffcierCia/DeFi-Developer-Road-Map#mev---maximal-extractable-value--miner-extractable-value) |
|     툴 모음      | [Explore](https://github.com/OffcierCia/DeFi-Developer-Road-Map#tools-collection)                                         |
|   이더리움 2.0   | [Explore](https://github.com/OffcierCia/DeFi-Developer-Road-Map#ethereum-20)                                              |
|   프론트 엔드    | [Explore](https://github.com/OffcierCia/DeFi-Developer-Road-Map#front-end)                                                |

# Basics:

- 분산장부 기술의 기본 알아보기 (DLT)
- 비트코인 프로토콜 [설명](https://medium.com/coinmonks/bitcoin-white-paper-explained-part-1-4-16cba783146a)
- 타원곡선암호 (Elliptic Curve) [암호학](https://medium.com/coinmonks/learn-how-to-code-elliptic-curve-cryptography-a952dfdc20ab)
- 읽기: [블록체인 설명](https://www.investopedia.com/terms/b/blockchain.asp)
- 보기: [블록체인 - 시각화 데모](https://www.youtube.com/watch?v=_160oMzblY8)

#### 이더리움

- 이더리움의 기본 알아보기
- 이더리움 가상 머신 (EVM): 튜링 완전 지갑, 계정 (EOA), 비밀키/개인키
- 트렌젝션(transactions), 가스(Gas), 메타마스크(Metamask)
- 이더리움 클라이언트/노드, Geth
- Infura infrastructure

#### 스마트 컨트랙트

- 스마트 컨트랙트의 기본
- 스마트 컨트랙트의 라이프 사이클 알아보기
- 이더리움 상위 레벨 언어 (**솔리디티(Solidity)**, Vyper, LLL, Serpent)
- 컴파일, 테스트, 스마트 컨트랙트 배포
- web3.js 또는 web3.py를 이용한 스마트 컨트랙트 적용
- [이더리움은 어떻게 작동할까요?](https://medium.com/@preethikasireddy/how-does-ethereum-work-anyway-22d1df506369)
- 읽기: [이 글](https://blog.zeppelin.solutions/the-hitchhikers-guide-to-smart-contracts-in-ethereum-848f08001f05)
- 읽기: [Truffle 공식문서](https://truffleframework.com/docs/) / [Hardhat Documentation](https://hardhat.org/getting-started/)
- 읽기: [Web3 공식문서](https://web3js.readthedocs.io/en/1.0/) / [Ethers Documentation](https://docs.ethers.io/v5/)
- 읽기: [이더리움 마스터](https://github.com/ethereumbook/ethereumbook)
- 읽기: [솔리디티 스마트 컨트랙트 라이브러리](https://openzeppelin.org/api/docs/get-started.html)

#### 스마트 컨트랙트 표준

- [ERCs](https://eips.ethereum.org/erc) - 이더리움 개선안

#### 토큰

- [ERC-20](https://eips.ethereum.org/EIPS/eip-20) - 유동성 자산에 대한 토큰 컨트랙트.
- [ERC-721](https://github.com/ethereum/eips/issues/721) - 비휘발성 자산의 토큰 표준.
- [ERC-918](https://eips.ethereum.org/EIPS/eip-918) - 채굴 가능한 토큰의 표준.

#### 기타

- [ERC-165](https://eips.ethereum.org/EIPS/eip-165) - 스마트 컨트랙트가 구현하는 인터페이스를 알아보고 이용하는 표준방법
- [ERC-725](https://eips.ethereum.org/EIPS/eip-725) - 단순 프록시 계정을 위한 표준 인터페이스
- [ERC-173](https://eips.ethereum.org/EIPS/eip-173) - 컨트랙트 소유권을 위한 표준 인터페이스

#### 일반적인 개발 기술들

- Learn [GIT](https://medium.com/pixel-pioneers/the-basics-of-version-control-system-git-explained-by-designing-a-new-car-3fb3a10e9e40)
- 레파지토리를 생성하는 방법 [GitHub](https://github.com/) / [GitLab](https://about.gitlab.com/)
- 당신의 코드를 사람들에게 공개하는 방법: HTTP(S) 통신 규약, request methods (GET, POST, PUT, PATCH, DELETE, OPTIONS)
- 구글을 사용하는 것을 두려워하지 마세요, [구글 검색 더 잘하는법](http://www.powersearchingwithgoogle.com/)
- 터미널에 익숙해지기 ([Linux/Docker](https://medium.com/coinmonks/how-to-become-a-blockchain-developer-59c830e20f15)), 당신의 쉘 설정(bash, zsh, fish)
- 알고리즘, 데이터 구조, 블록체인, 이더리움, 견고성에 대한 책을 읽어보세요.
- 이 코스를 해보세요.[이더리움 그리고 솔리디티: 완벽 개발자 가이드](https://www.udemy.com/ethereum-and-solidity-the-complete-developers-guide/)
- 무료 자습서 [솔리디티 배우기](https://github.com/willitscale/learning-solidity)
- [솔리티디를 이용한 스마트 컨트랙트 소개](https://www.youtube.com/playlist?list=PLV1JDFUtrXpGvu8QHL9b78WYNSJsYNZsb)

#### 이 도구을 사용해보세요:

- [eth-cli](https://github.com/protofire/eth-cli) - CLI tools.
- [REPL](https://github.com/raineorshine/solidity-repl) - 솔리디티 REPL.
- [Remix](https://remix.ethereum.org/) - 온라인 실시간 컴파일러 그리고 런타임.

# dApps

- 사용할 도구에 익숙해지세요.

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

- [크립토 좀비](https://cryptozombies.io/)을 통해 이더리움 개발 학습
- 예제를 읽고 만들어보세요: [펫 샵 자습서](https://www.trufflesuite.com/tutorial)
- [시간 잠금 지갑: 이더리움 스마트 컨트랙트 소개](https://www.toptal.com/ethereum-smart-contract/time-locked-wallet-truffle-tutorial)
- [The Ultimate ENS 그리고 ĐApp 자습서](https://www.toptal.com/ethereum/ethereum-name-service-dapp-tutorial)
- [Ultimate Introduction to Ethereum Ðapp Development](https://www.youtube.com/playlist?list=PLV1JDFUtrXpFh85G-Ddyy2kLSafaB9biQ)
- [Ethernaut](https://ethernaut.zeppelin.solutions/) is a Web3/Solidity based wargame for those interested in learning ethereum
- [이더리움 그리고 솔리디티: 완벽 개발자 가이드](https://www.udemy.com/ethereum-and-solidity-the-complete-developers-guide/)
- [Consensys 모범 사례](https://consensys.github.io/smart-contract-best-practices/) - 이 문서는 중간에 솔리디티 프로그래머의 보안 사항에 대한 기본 지식을 제공하며 ConsenSys Diligence와 더 넓은 이더리움 커뮤니티로 유지합니다.
- [솔리디티 패턴](https://github.com/fravoll/solidity-patterns) - 패턴과 모범 사례 모음입니다.

# 영지식 증명(ZK-SNARKs)

#### 일반적인 정보

- [ZoKrates](https://github.com/Zokrates/ZoKrates) - 이더리움에서 zkSNARKS을 위한 도구상자
- [The AZTEC Protocol](https://github.com/AztecProtocol/AZTEC) - 이더리움 네트워크에서 거래 및 구현은 메인넷에서 진행됩니다.
- [Nightfall](https://github.com/EYBlockchain/nightfall) - ERC-20 / ERC-721 개인 토큰 - 오픈 소스도구 & 마이크로 서비스 만들기
- 프록시 재암호화 (PRE)
- [NuCypher Network](https://github.com/nucypher/nucypher) - 분산된 시스템에서 개인 정보 보호를 강화하기 위한 프록시 재암호화 네트워크
- [pyUmbral](https://github.com/nucypher/pyumbral) - 임계값 프록시 재암호화 라이브러리
- 완전 동형 암호화 (FHE)
- [NuFHE](https://github.com/nucypher/nufhe) - GPU 가속화 FHE 라이브러리

#### 영지식 증명(ZK-SNARKs)

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
- [Brownie](https://github.com/iamdefinitelyahuman/brownie) - Brownie는 이더리움 스마트 컨트랙트를 구현, 테스트 및 상호작용하기 위한 파이썬 프레임워크입니다.
- [Embark](https://github.com/embark-framework/embark) - DApp 개발자를 위한 프레임워크
- [Waffle](https://getwaffle.io/) - 고급 스마트 컨트랙트 개발 및 테스트를 위한 프레임워크로 작고, 빠르고, 유연하며, 신속합니다.(ether.js 기반)
- [Dapp](https://dapp.tools/dapp/) - DApp 개발을 위한 프레임 워크, 성공적인 DApple의 후계자
- [Etherlime](https://github.com/LimeChain/etherlime) - ethers.js 기반 Dapp 개발 프레임워크
- [Parasol](https://github.com/Lamarkaz/parasol) - 테스트, INFURA 구축, 자동 컨트랙트 문서등을 지원하는 프레임워크로 애자일하며 개발 환경이 유연하고 자유로운 디자인으로 사용자 지정에 제한이 없습니다.
- [0xcert](https://github.com/0xcert/framework/) - 분산 애플리케이션 구축을 위한 자바스크립트 프레임워크
- [OpenZeppelin SDK](https://openzeppelin.com/sdk/) - OpenZeppelin SDK: 스마트 컨트랙트을 개발, 컴파일, 업그레이드, 배포 및 상호 작용에 도움이 되는 도구 모음입니다.
- [sbt-ethereum](https://sbt-ethereum.io/) - 지갑 및 ABI 관리, ENS 지원, 고급 스칼라 통합을 비롯한 스마트 컨트랙트 상호 작용 개발을 위한 탭 기반 텍스트 콘솔입니다.
- [Cobra](https://github.com/cobraframework/cobra) - 이더리움 스마트 컨트랙트, 테스트 및 EVM(Ethereum virtual machine) 구축을 위한 빠르고 유연하며 단순한 개발 환경 프레임워크 입니다.
- [Epirus](https://docs.epirus.io/sdk/) - 스마트 컨트랙트을 구축하기 위한 자바 프레임워크

#### 스마트 컨트랙트과 상호 작용

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
- [Cliquebait](https://github.com/f-o-a-m/cliquebait) - 실제 블록체인 네트워크와 매우 유사한 도커 인스턴스를 통해 스마트 컨트랙트 애플리케이션의 통합 및 테스트 수용을 간소화 할 수 있습니다.
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

- 리액트 [공식 사이트](https://reactjs.org/tutorial/tutorial.html) 또는 [코스](https://egghead.io/courses/the-beginner-s-guide-to-react)를 배울 수 있습니다.
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
- [스마트 컨트랙트 배우기](https://github.com/arbazkiraak/SmartContractLearning)
- [멋진 암호화폐 사회](https://github.com/jpantunes/awesome-cryptoeconomics)

#### 보안과 안전:

- [호루스의 눈: 이더리움 스마트 컨트랙트에 대한 공격 분석](https://arxiv.org/pdf/2101.06204.pdf) - 조사결과, 지난 몇 년간 공격 횟수가 감소하지는 않았지만 일부 취약점의 경우 일정하게 나타나고 있습니다.

- [대규모 거래를 통한 비트코인 Bribery 취약점 분석](https://arxiv.org/pdf/2105.07501.pdf) - 이 문서의 저자는 새로운 Bribery 공격을 기획하고 이 개런티가 크게 훼손될 수 있음을 보여줍니다.

- [양자 공격에 대한 블록체인 기술의 취약성](https://arxiv.org/pdf/2105.01815.pdf) - 저자는 비트코인, 이더리움, 라이트코인, 지캐시 등 현존하는 주요 블록체인 기반 암호화폐를 분석해 양자 공격에 대한 위험 노출도를 파악합니다.

- [BLOCKEYE](https://arxiv.org/pdf/2103.02873.pdf) - 블록체인 디파이(DeFi) 공격을 잡는 법을 소개하며 본 문서에서 저자는 실시간 공격 탐지 시스템인 BLOCKEYE를 제안합니다.

- [동적 다중 계층 블록체인 네트워크의 위상적 이상 감지](https://arxiv.org/pdf/2106.01806.pdf) - 저자는 동적 다계층 네트워크에서 구조적 이상 징후 감지에 대한 새로운 위상학적 관점을 소개합니다.

- [Dafny를 이용한 머클트리(Merkle Tree) 증분 알고리즘 검증](https://arxiv.org/pdf/2105.06009.pdf) - 저자는 Dafny 확인 가능한 기계 가능(machine-checkable)버전과 알고리즘에 대한 새롭고 독창적인 정확성 증명에 대한 부분을 소개합니다.

- [GoHammer 블록체인 성능 테스트 도구](https://arxiv.org/pdf/2105.00847.pdf) - GoHammer는 효율적인 분산형 시스템을 개발하는 데 도움이 되며 분산형 애플리케이션 프로젝트 개발 비용 절감에 영향을 줍니다.

- [EtherClue: 이더리움 스마트 컨트랙트서 공격 디지털 조사 ](https://arxiv.org/pdf/2104.05293.pdf) - 저자는 이 연구에서 블록체인에 사용하기 위해 특수 제작된 Indicators of Comprehorise를 이용하여 이더리움 공격의 사후 분석 문제를 연구합니다.

- [활용 사례별 블록체인 플랫폼 요구사항 분석 및 평가](https://arxiv.org/pdf/2103.03209.pdf) - 이 문서에서는 블록체인과 응용 프로그램을 이해하기 위한 일반적인 모델을 제공합니다.

- [상수 함수에서 마켓 메이커의 프라이버시에 관한 참고 사항](https://arxiv.org/pdf/2103.01193.pdf) - 이 문서에는 저자는 가장 합리적인 상대 모델에서 CFMM의 일반적인 구현으로 프라이버시가 불가능하며 일부 완화 전략을 제공한다는 것을 보여줍니다.

- [이더리움 스마트 컨트랙트의 보안 취약점 조사](https://arxiv.org/pdf/2105.06974.pdf) - 이 문서는 이더리움 스마트 컨트랙트의 취약성의 활용 사례를 분석하며 BT 애플리케이션 레벨에 특정한 8가지 취약점에 대해 설명합니다.

- [이더리움 스마트 컨트랙트의 서비스 거부 취약점 감지 방법](https://arxiv.org/pdf/2106.01340.pdf) - 이 문서는 저자가 이더리움 스마트 컨트랙트의 예상치 못한 되돌림으로 DoS를 감지하기 위해 정적 분석과 동적 분석을 결합한 프레임 워크를 제안합니다.

- [AGSolT: 자동화된 테스트 사례 생성 도구(솔리디티 스마트 컨트랙트)](https://arxiv.org/pdf/2102.08864.pdf) - 저자는 AGSoIT가 두 가지 접근 방식으로 높은 지점 초과를 달성할 수 있다는 것을 발견했으며 Github에서 가장 인기 있는 솔리디티 스마트 컨트랙트에서 몇 가지 오류를 발견했습니다.

- [이더리움 거래 추적을 위한 시간량 스냅샷 다중 그래프](https://arxiv.org/pdf/2102.08013.pdf) - 저자는 TASMG를 제안하여 이더리움 거래 기록을 시간적 금액의 네트워크로 모델링 한 후 TAW를 제시함으로써 제안된 네트워크의 시간적 및 금액 정보를 통합한 거래 기록을 통해 계정을 효과적으로 임베딩할 수 있도록 합니다.

- [암호화폐 마이닝 공격: 디지털 포렌식 및 동적 네트워크 특성에 기반한 준감독 학습 방식](https://arxiv.org/pdf/2102.10634.pdf) - 이 문서는 동적 네트워크 특성을 사용하는 일반 네트워크 환경에서 암호화 마이닝 공격의 탐지를 다루고 있습니다.

- [FASTEN: 스마트 컨트랙트을 이용한 공정하고 안전한 분산 투표](https://arxiv.org/pdf/2102.10594.pdf) - 저자는 사생활 침해의 가능성이 극히 접다는 것을 증명했으며, 이더리움을 통한 FINSE 실행 비용 분석은 대부분 기존 선거 비용과 비교할 수 있음을 이야기합니다.

- [마이닝 비용, 마이닝 보상 및 블록체인 보안 간 상호 의존성](https://arxiv.org/pdf/2102.08107.pdf) - PoC(Proof-of-Work) 블록체인 운영 비용이 공격 방지 비용과 본질적으로 연관이 있으며, 디지털 기반 원장 보안 예산이 암호화폐 시장에 얼마나 연관이 있는지에 대한 연구문서입니다.

- [HyperSec: 블록체인 보안 모니터링 시각적 분석](https://arxiv.org/pdf/2103.14414.pdf) - HyperSec, 하이퍼레저 패브릭에 대한 지속적인 공격을 감지하기 위한 관련 정보를 한눈에 제공하는 시각적 분석 모니터링 도구입니다.

- [이더리움 스마트 컨트랙트의 재진입 취약성 식별](https://arxiv.org/pdf/2105.02881.pdf) - 이 문서에서는 저자는 정적 분석과 동적 분석을 결합하여 이더리움 스마트 컨트랙트의 Reentrancy 취약성을 탐지하는 프레임워크를 제시합니다.

- [IMT2000 3GPP - 블록체인 프로토콜의 보안 분석을 위한 일반 프레임워크](https://arxiv.org/pdf/2009.09480v2.pdf) - 이 문서는 잘 알려진 무허가 블록체인 프로토콜의 속성을 보여주고 비교하기에 충분하고 인색한 추상화를 제시합니다.

- [코인 버그들: 일반적인 블록체인 구현 수준 취약성 열거](https://arxiv.org/pdf/2104.06540.pdf) - 이 문서는 공통적인 블록체인 보안 리뷰와 블록체인 개발 시작을 목표로 하는 보안 테스터를 대상으로 공통적인 함정과 참고자료를 제시합니다.

- [스마트 컨트랙트의 취약성 및 미해결 문제: 체계적 매핑](https://arxiv.org/pdf/2104.12295.pdf) - 이 문서는 SC를 분석하기 위한 이니셔티브 도구와 식별된 취약점을 처리하는 방법을 체계적인 문헌을 통해 분석했습니다.

- [SuMo: 고형성 스마트 컨트랙트을 위한 돌연번이 테스트 전략](https://arxiv.org/pdf/2105.03626.pdf) - 저자는 테스트 스위트(test suite)를 이용한 오픈 소스 프로젝트에서 얻은 평가를 보고하고 있습니다. SoMo가 개발자들이 보다 신뢰할 수 있는 스마트 컨트랙트을 제공할 수 있도록 효과적으로 도울 수 있다고 제안하고 있습니다.

- [블록체인의 안정성: 나선형 파괴와 스테이블 코인 공격](https://arxiv.org/pdf/1906.02152.pdf) - 나선형 파괴 가능성은 2019년부터 예측됬고 2020년 Dai 위기의 검은 목요일 사태에서 관측됬습니다.

- [블록체인 시스템에 대한 익명 신탁제도](https://arxiv.org/pdf/2010.00206.pdf) - 이 문서에서 저자는 모든 암호화폐에 적용되는 블록체인 시스템에 대해 익명의 신탁 표시 제도를 제안합니다.

- [이더리움 스마트 컨트랙트에서 버그를 위한 프레임워크 및 데이터셋](https://arxiv.org/pdf/2009.02066.pdf) - 이 문서에는 먼저 여러 소스들로 최대한 많은 스마트 컨트랙트 버그를 수집하고 IEEE 표준 소프트웨어 이상 분류를 확장하여 이러한 버그를 9가지 범주로 나눕니다.

- [블록체인 네트워크의 다양한 마이너 공격에 대한 안전한 멀티체인 컨센서스 제도](https://arxiv.org/pdf/2106.02383.pdf) - 실험 결과에 따르면 PoDT는 DMB 공격으로부터 안전하며 멀티 체인 환경에서 기존의 합의 방식보다 더 효과적이라고 말합니다.

- [컨소시엄 블록체인 컨센서스 메커니즘 조사](https://arxiv.org/pdf/2102.12058.pdf) - 이 문서에서는 엔터프라이즈 블록체인의 컨센서스 알고리즘에 포함된 몇 가지 최신 솔루션을 중점으로 다룹니다.

- [Coq에서 테스트와 검증된 스마트 컨트랙트 추출](https://arxiv.org/pdf/2012.09138.pdf) - 저자는 MetaCoq의 인증된 삭제를 기반으로 기능 언어로 Coq 프로그램을 추출합니다.

- [신뢰 할 수 없는 개인 정보 보호 블록체인 브릿지](https://arxiv.org/pdf/2102.04660.pdf) - 브릿지의 프라이버시를 보호하는 신뢰없는 교차 체인 암호화폐 전송을 촉진하기 위한 프로토콜을 제시한 문서입니다.

- [이더리움 스마트 컨트랙트 개발을 위한 보안 체크리스트](https://arxiv.org/pdf/2008.04761.pdf) - 소프트웨어 라이프사이클의 설계, 코딩, 테스트와 구현 단계를 다룬 문서입니다.

- [머신러닝을 이용한 스마트 컨트랙트에서의 동적 취약성 탐지](https://arxiv.org/pdf/2102.07420.pdf) - 이더리움 스마트 컨트랙트의 재진입 취약성을 감지하기 위한 모니터링 프레임워크인 Dynamit을 제안하는 문서입니다.

- [가장 취약한 링크: 이더리움 스마트 컨트랙트의 소셜 공격](https://arxiv.org/pdf/2105.00132.pdf) - 스마트 컨트랙트 허니팟을 넘어 새로운 소셜 공격의 가능성을 탐구한 문서입니다.

- [OptSmart: 공간 효율적인 스마트 컨트랙트의 동시 실행](https://arxiv.org/pdf/2102.04875.pdf) - optimistic Software Transactional Memory systems (STMs)을 사용하여 AU를 동시에 실행하여 블록 실행하는 동시 마이너를 개발하는 것을 담은 문서입니다.

- [DEFECTCHECKER: EVM 바이트 코드 분석을 통한 자동화 스마트 컨트랙트 결함 감지](https://arxiv.org/pdf/2009.02663.pdf) - 실험 결과에 따르면 속도와 정확성 측면에서 결점 검사기가 이러한 도구보다 훨씬 뛰어난 성능을 발휘합니다.

- [SmartBugs: 견고성 스마트 컨트랙트 분석 프레임워크](https://arxiv.org/pdf/2007.04771.pdf) - DASP10 범주 무작위성, 시간 조작 그리고 엑세스 컨트롤 관련된 취약점 검출을 크게 개선하는 도구 SmartCheck를 통해 분석 도구의 손쉬운 통합과 비교를 가능하게 만드는 방법을 보여줍니다.(식별된 취약점이 11%에서 24%로 증가했습니다.).

- [고형성 스마트 컨트랙트의 가스 누출 프로파일링](https://arxiv.org/pdf/2008.05449.pdf) - 본 문서에서 저자들은 스마트 컨트랙트의 구축과 거래 비용에 영향을 미치는 19가지 코드를 식별하고 34명의 참가를 대상으로 한 설문조사를 통해 관련성을 평가합니다.

- [가변 마이닝 파워로 병렬 체인 프로토콜 보호](https://arxiv.org/pdf/2105.02927.pdf) - 이 문서에 저자들은 그러한 마이닝 파워변화에 적응할 수 있는 안전한 병렬 체인 프로토콜의 설계를 고려합니다.

- [Deep Neural Network 및 Transfer Learning을 이용한 이더리움 스마트 컨트랙트 취약성 감지](https://arxiv.org/pdf/2103.12607.pdf) - ERCORT 프레임워크는 DNN 모델 아키텍처의 최소한의 수정과 재교육 오버헤드를 통해 새로운 취약점 유형에 대한 이전 학습을 가능하게 합니다.

- [SCSGuard: 이더리움 스마트 컨트랙트을 위한 심층 사기 탐지](https://arxiv.org/pdf/2105.10426.pdf) - 실험 결과는 SCSGuard가 Ponzi 및 Honeypot 스캠과 새로운 피싱 스마트 컨트랙트에 대해 높은 정확도(0.94), 정밀도(0.96%) 및 리콜(0.98)을 달성하는 것으로 나타났습니다.

- [블록체인 기반 디지털 트윈과 보안 위협 인텔리전스를 통한 사이버 물리적 시스템 보안](https://arxiv.org/pdf/2105.08886.pdf) - 이 문서에서는 인텔리전트하고 신뢰할 수 있는 DT를 위해 인공지능(AI)과 블록체인을 통합하여 CPS를 보호하는 방법을 중점적으로 다룹니다.

#### 디파이(DeFI)

- [복합 디파이 프로토콜의 공식 분석](https://arxiv.org/pdf/2103.00540.pdf) - In this paper, authors propose a formal process-algebraic technique that models DeFi protocols in a compositional manner to allow for efficient property verification.

- [거래 수수료 체계 설계](https://arxiv.org/pdf/2106.01340.pdf) - 저자는 블록체인 수수료에 대해 설명합니다.

- [DeFi-ning DeFi: 과제와 경로](https://arxiv.org/pdf/2101.05589.pdf) - 탈중앙화 금융 시작에 대한 좋은 회고.

- [디파이 시장 자동화에 대한 이론](https://arxiv.org/pdf/2102.11350.pdf) - 구조와 경제적 측면을 모두 특정짓는 일련의 AMM의 기본 특성을 공식적으로 증명하기 위한 이론을 이용합니다.

- [은행에서 디파이로: 대출 시장의 발전](https://arxiv.org/pdf/2104.00970.pdf) - 전통적인 금융 시스템에 대한 디파이 대출의 지속적인 의존도에 대해 논의하고 IOV 시대의 대출 시장 전망을 가지고 결론을 내립니다.

- [디파이 프로토콜에서 수익 창출 트랜잭션의 적시 발견에 관한 연구](https://arxiv.org/pdf/2103.02228.pdf) - 수익성 있는 디파이 거래를 자동으로 생성할 수 있는 두 가지 방법을 조사합니다.
- [자동화된 시장 제조업체에서 추출 가능한 가치 극대화](https://arxiv.org/pdf/2106.01870.pdf) - 공식적으로 이성적인 채굴자들을 채굴의 최적 전략을 따르는 참가자로 규정합니다.

- [탈중앙화 금융의 위기](https://arxiv.org/pdf/2002.08099.pdf) - 이 문서는 설계상 약점과 가격 변동이 어떻게 디파이 위기를 초래할 수 있는지 살펴봅니다.

- [청산, 칼날 위의 디파이](https://arxiv.org/pdf/2009.13235v4.pdf) - 고통스러운 손실로부터 프로토콜을 보호하기 위해 과소하게 담보화된 포지션은 청산될 수 있습니다. 대출가능자금 프로토콜(PLF)에 대한 청산 경험적 분석을 제사합니다.

- [디파이 통합을 위한 프록시로 자산 합성 가능성 측정](https://arxiv.org/pdf/2102.04227.pdf) - 2020년 계산된 전체 3억4480만건의 이더리움 거래 집합에 대해 자산 DAI, USDC, USDT, ETH 그리고 토큰화된 BTC의 '복합'파생상품 거래를 검토하고 이러한 관행이 이더리움 금융 통합에 어느 정도 기여할 수 있는 파악하는 문서입니다.

- [탈중앙화 자율 암호화폐 거래소의 동적 곡선](https://arxiv.org/pdf/2101.02778.pdf) - 이 연구에서 동적 곡선 개념을 제안함으로써 AMM을 구성하는 새로운 접근 방식을 제안합니다.

- [탈중앙화 온체인 거래소의 High-Frequency 트레이딩](https://arxiv.org/pdf/2009.14021.pdf) - 전방, 후방 피해자 TX르르 포함하는 전방 실행의 증강된 변현 샌드위치 공격을 공식화, 분석적 노출 및 경험 평가에 대한 문서입니다.

- [Flashot](https://arxiv.org/pdf/2102.00626.pdf) - 디파이 에코시스템에 대한 플래시론 공격 기록입니다.

- [DeFiRanger](https://arxiv.org/pdf/2104.15068.pdf) - 디파이 애플리케이션에 대한 가격 조작 공격 탐지

- [재미와 수익을 위한 플래시론 디파이 에코시스템 공격들](https://arxiv.org/pdf/2003.03810.pdf) - 플래시론. 디파이. 클래식.

- [SoK: 탈중앙화 금웅 (DeFi) ](https://arxiv.org/pdf/2101.08778.pdf) - SoK에서 주요 축을 따라 디파이 생태계를 설명합니다. SCSGuard: 이더리움 스마트 컨트랙트을 위한 딥 스캠
- [4가지 거버넌스 토큰 분포의 경험적 증거](https://arxiv.org/pdf/2102.10096.pdf) - 블록체인 애플리케이션 간의 지배력 분산을 정량화할 수 있는 프레임워크를 제공합니다.

- [블록체인 기반 탈중앙화 거래소 도입](https://arxiv.org/pdf/2103.08842.pdf) - 블록체인 기반 거래소의 주문 실행 매커니즘으로 환율이 변동하면 윧동성 제공자들이 토큰 가치를 잃는다는 것을 보여줍니다.

- [유니스왑 시장 분석](https://arxiv.org/pdf/1911.03380.pdf) - 유니스왑 DEX 활동에 대한 최고의 연구 중 하나로 2019년에 연구를 시작했고 2021년에 새로운 분석을 발표했다.

- [금융 4.0: 지속 가능성을 다루기 위한 가치에 민감한 암호화 경제 시스템의 설계 원칙](https://arxiv.org/pdf/2105.11955.pdf) - 암호화 시스템 설계에 대한 새로운 통찰력을 제공합니다.

- [탈중앙화 거래소 유동성 제공자의 행태](https://arxiv.org/pdf/2105.13822.pdf) - 유동성 제공자들이 시장 정보에 어떻게 반응하고 그들이 유동성 공급으로부터 어떻게 이익을 얻는지를 이해하는 것을 목표로 합니다.

- [탈중앙화 거래소 시장의 주기적 재정거래](https://arxiv.org/pdf/2105.02784.pdf) - 스마트 컨트랙트 기술과 이더리움의 복제된 상태 기계 설정을 통해 자금 거래 전략이 CEX보다 DEX에서 더 쉽게 구현될 수 있음을 시사합니다.

- [SoK: Ground Truth에서 시장조작으로 이어지는 오라클](https://arxiv.org/pdf/2106.00667.pdf) - SoK에서 오라클에 대한 설계 대안을 시스템화하고, 공격을 선보이며, 공격 완화 전략을 논의합니다.

- [자동화된 시장 제조업체들의 네트워크 구성](https://arxiv.org/pdf/2106.00083.pdf) - AMM 구성을 위한 수학적 모델 제안

#### 이더리움 이름 서비스

- [이더리움 이름 서비스: 선, 악, 추함](https://arxiv.org/pdf/2104.05185.pdf) - ENS의 보안 문제 및 잘못된 행동, 새롭게 부상하는 시스템에 대해 연구한 기존 연구는 없습니다. 저자는 ENS와 관련된 수백만 개의 이벤트 로그를 분석하여 ENS의 첫번째 연구를 제시합니다.

#### 대체 불가능 토큰 (NFT)

- [NFT 혁명 매핑](https://arxiv.org/pdf/2106.00647.pdf) - 시장 동향, 거래 네트워크 및 시각적 특징

- [ERC 토큰 시장의 공정성](https://arxiv.org/pdf/2102.03721.pdf) - CryptoKitties의 사례 연구.

- [대체 불가능 토큰: 개요, 평가, 기회와 과제](https://arxiv.org/pdf/2105.07447.pdf) - 여러 측면에서 NFT 에코시스템을 탐색합니다.

- [Cryptoart](http://cryptoart.io/) - 탑 아티스트와 저작물.

- [CryptoArtPulse](https://cryptoartpulse.com/) - 라이브뷰

- [PumpMyGas](https://pumpmygas.xyz/) - 모든 주요 NFT 시장의 가스 요금 추정치

- [NonFungible Tracker](https://nonfungible.com/) - NFT 트래커.

- [NFTS TOP](https://cryptoslam.io) - NFT 랭킹.

#### 스테이블 코인

- [스테이블 코인 2.0](https://arxiv.org/pdf/2006.12388.pdf) - 스테이블 코인의 경제구조에 대한 리스크 기반 기능적 특성으로 스테이블 코인 이론을 위한 탄탄한 토대를 마련하고자 합니다.

- [가상화폐의 변동성 축소 - 안정적 코인 조사](https://arxiv.org/pdf/2103.01340.pdf) - 스테이블 코인의 안정성 메커니즘을 조사함으로 암호화폐의 변동성을 줄이는 데 어떻게 도움이 되는지 논의합니다.

- [알고리즘 스테이블 코인의 변동성 이해: 모델링, 검증 및 경험적 분석](https://arxiv.org/pdf/2101.08423.pdf) - Basis Cashstable Coin의 실거래 활동에 대한 체계적인 경험적 분석을 수행하여 이론적 가능성을 시장 관찰과 연관시켰습니다.

- [T-Cash: 야동 가능한 Fiat Backed 코인](https://arxiv.org/pdf/2105.04485.pdf) - 시스템 내에서 코인을 지속적으로 재사용할 수 있는 블록체인 기술을 이용한 이전 가능한 전자 현금 제도를 제안합니다.

#### 일반적인 정보:

- [이더리움 네트워크의 빅데이터 분석: 블록체인부터 구글 트렌드 까지](https://arxiv.org/pdf/2104.01764.pdf) - 암호화폐 가격과 검색 트렌드를 분석한 결과, 일반 사용자가 아닌 대형 업체들이 시장을 조정하는 것으로 나타났습니다.

- [원자성과 확장 가능한 거래를 위한 DLT 기반 스마트 컨트랙트 아키텍처](https://arxiv.org/pdf/2105.02937.pdf) - 안전하고 동적으로 업데이트할 수 있는 확장 가능하고 개인 정보를 보호하는 원자성 프로토콜을 제안합니다.
  그런 다음 차염자가 주 채널을 초기화하기 전에 자금을 잠글 수 있는 스마트 컨트랙트 기반 CNS(Credit-Note System)을 개발하여 유연성과 효율성을 높입니다.

- [이더리움 데이터 저장소 탐색](https://arxiv.org/pdf/2105.10520.pdf) - 이더리움 애플리케이션에 대한 포괄적인 데이터 관리 접근방식을 검토하고 관련 가스 비용 및 검색 성능을 평가합니다.

- [블록체인 거버넌스에 관한 체계적 문헌 검토](https://arxiv.org/pdf/2105.05460.pdf) - 5W1H 질문을 통해 블록체인 거버넌스를 종합적으로 조사합니다.

- [블록체인 분석을 위한 일반적인 프레임 워크](https://arxiv.org/pdf/1707.01021.pdf) - 비트코인 이더리움에서 데이터 분석을 지원하는 범용 프레임워크를 제안합니다. 블록 데이터를 다른 소스의 데이터와 통합하고 데이터베이스에 정리할 수 있습니다.

- [AMR: 보상 분배를 위한 프라이버시 기능을 갖춘 자율 코인 믹서](https://arxiv.org/pdf/2010.01056.pdf) - 시스템에 참여하는 사용자에게 프라이버시 보존 방식으로 보상할 수 있는 최초의 검열 복원력 있는 믹서를 제안합니다.

- [블록체인 데이터 개인 정보 보호 솔루션의 기술 검토](https://arxiv.org/pdf/2105.01316.pdf) - 기존 엔터프라이즈 블록체인 기술인 EOSIO 기반 시스템, 하이퍼레저 패브릭 그리고 Besu, Consensus Quarum, R3 Corda 및 Ernst and Young's Nightfall을 검토하는 것을 목적으로 합니다.

- [블록체인 시스템, 기술 그리고 애플리케이션 방법론의 관점](https://arxiv.org/pdf/2105.03572.pdf) - 첫째, 블록체인의 작동 방식, 연구 활동 및 과제를 소개하고 전형적인 블록체인 사용 사례와 주제에 대한 전형적인 방법론을 다루고 있는 로드맵을 보여줍니다.
  둘째, 블록체인 시스템에서 확률적 프로세스, 게임이론, 최적화, 머신러닝, 암호학을 채택하여 블록체인 프로토콜/알고리즘을 연구할 수 있는 방법에 대해 자세히 설명합니다.

- [Ethna: 이더리움 블록체인의 P2P망 분석](https://arxiv.org/pdf/2010.01373.pdf) - Ethna는 이더리움 노드의 정도를 정확하게 측정하는 새로운 방법을 구현합니다.

- [블록체인 소셜 네트워크에서의 커뮤니티 감지](https://arxiv.org/pdf/2101.06406.pdf) - 그래프의 낮은 순위 신호를 위해 설계된 새로운 커뮤니티 감지 알고리즘은 사용자 토큰 구독을 기반으로 사용자의 커뮤니티를 찾는데 도움이 될 수 있습니다.

- [무선 블록체인 네트워크의 블록 액세스 제어: 설계, 모델링 분석](https://arxiv.org/pdf/2104.13144.pdf) - BAC 접근 방식은 네트워크가 높은 트랜잭션 처리량을 달성하는 동시에 블록 활용률을 높이고 컴퓨팅 성능을 점감하는데 도움이 될 수 있다는 것을 알 수 있습니다. 한편, 트랜잭션 처리량과 블록 활용률 간의 균형을 입증하여, 실제적인 블록체인 구축을 위한 지침이 될 수 있습니다.

- [블록체인 및 분산원장 기술에 대한 외부적 요구](https://arxiv.org/pdf/2105.10399.pdf) - 블록체인 및 분산원장 기술이 블록체인/DLT 자체에서 시작된 외부 시스템에 대한 호출을 수행할 수 있는 방법을 시연함으로써 이러한 믿음이 선입견임을 보여줍니다.

- [블록체인 시스템 및 애플리케이션 관리: 블록체인 구성 프로세스 모델](https://arxiv.org/pdf/2105.02118.pdf) - 블록체인 구성 프로세스 모델이 4개의 블록체인 프로젝트에 적용된다는 것을 보여줍니다.

- [상설시장 운영사의 수수료 적정화 방안](https://arxiv.org/pdf/2105.13510.pdf) - 과거 거래 데이터를 사용하여 실제 세계 풀에 대한 최적의 수수료를 계산하는데 사용할 수 있는 프레임워크를 제시합니다.

- [진화 게임 이론을 이용한 블록체인 보상 메커니즘](https://arxiv.org/pdf/2104.05849.pdf) - PoS 블록 체인에 적용될 수 있는 보상 메커니즘 프레임워크를 개발합니다.

- [스마트 전환 요약](https://arxiv.org/pdf/2105.07663.pdf) - 무한한 균형 합계를 표현할 수 있는 1차 논리의 일반화를 제시합니다.

- [소프트웨어 신생 기업을 위한 100개 이상의 메트릭스 - 다중 음성 문학 리뷰](https://arxiv.org/pdf/1901.04819.pdf) - 데이터를 메트릭 형태로 사용하면 소프트웨어 신생 기업이 불확실성과 제한된 리소스 속에서 올바른 결정을 내리는 데 도움이 될 수 있습니다.

- [블록체인 네트워크: 비트코인, 모네로, 지캐시, 이더리움, 리플, 아이오타의 데이터 구조](https://arxiv.org/pdf/2103.08712.pdf) - 블록체인 데이터를 다양한 유형의 네트워크로 추상화할 수 있는 방법과 네트워크 추상화를 통해 구조에 대한 통찰력을 얻을 수 있습니다.

- [탈중앙화 금융: 블록체인 및 스마트 컨트랙트 기반 금융 시장](https://research.stlouisfed.org/publications/review/2021/02/05/decentralized-finance-on-blockchain-and-smart-contract-based-financial-markets) - Fabian Schar가 쓴 이 책은 기술적으로 상세하지만 소화할 수 있는 형식으로 블록체인 기반 시장에 대한 개요를 제공합니다. 새로운 사용자를 위한 훌륭한 논문입니다.

#### 사이드 체인들

- [POA Network](https://www.poa.network/)
- [POA Bridge](https://bridge.poa.net/)
- [POA Bridge UI](https://github.com/poanetwork/bridge-ui)
- [POA Bridge Contracts](https://github.com/poanetwork/poa-bridge-contracts)
- [Loom Network](https://github.com/loomnetwork)
- [Matic Network](https://docs.matic.network/)

#### EIP - 1559

- [EIP-1559 이더리움 수수료 시장의 동적 분석](https://arxiv.org/pdf/2102.10567.pdf) - 게임 이론과 동적 시스템 도구를 조합하여 시장의 동적 메커니즘을 철저한 분석합니다.
- [EIP1559 기본요금의 확률적 특성](https://arxiv.org/pdf/2105.03521.pdf) - 변동하는 가스 가격에 안정을 주기위해 개발된 이더리움의 새로운 가격 체계에 대해 설명합니다.

- [이더리움 블록체인을 위한 거래 수수료 메커니즘 설계: EIP-1559의 경제성 분석](https://arxiv.org/pdf/2012.00854.pdf) - 게임 이론적인 강점과 약점을 평가하고 몇 가지 대안 설계를 검토합니다.

#### 이더리움 2.0

- [Beaconcha](https://beaconcha.in/)
- [Beaconscan](https://beaconscan.com/)
- [이더리움 2.0 상태](https://eth2stats.io/)
- [이더리움 2.0 문서](https://docs.ethhub.io/ethereum-roadmap/ethereum-2.0/eth-2.0-phases/)
- [이더리움 2.0 클라이언트들](https://docs.ethhub.io/ethereum-roadmap/ethereum-2.0/eth2.0-teams/teams-building-eth2.0/)
- [이더리움 2.0 Forks](https://eth2-fork-mon.stokes.io/)

#### MEV - 최대 추출 가능 값 / 마이너 추출 가능값

- [블록체인 추출 가능 값 수량화: 숲은 얼마나 어둡습니까?](https://arxiv.org/pdf/2101.05511v2.pdf) - 광부들이 이미 MEV(Miner Extractable Value)를 추출하고 있다는 증거를 제시하는데, 이는 관련 연구에서 알 수 있듯이 블록체인 컨센서스 보안을 불안정하게 할 수 있습니다.

- [Flash Boys 2.0: 분산형 Exchange의 프런트런닝, 트랜잭션 재주문 및 컨센서스 불안정성](https://arxiv.org/pdf/1904.05234.pdf) - MEV의 개념을 소개하고, 스마트 컨트랙트의 거래 순서 의존성에 의해 야기되는 크고 복잡한 위험과 전통적인 형태의 금융 시장 착취가 블록체인 경제에 적응하고 침투하는 방법을 가종합니다.

- [Flashbots: MEV in Eth2](https://hackmd.io/@flashbots/mev-in-eth2) - eth2의 거래 순서를 연구하고 MEV 기반 스테이킹 수익률을 분석합니다. 그리고나서 MEV가 검증자 보상을 상당히 증가시키겠지만 eth2의 참가자 사이의 불평등을 강화시킬 수 있다는 것을 발견합니다. 저자는 교환 및 검증자 풀과 같은 최대 이해관계자들 사이에 전개될 잠재적 역학같은 eth2의 MEV의 질적 측면을 논의합니다.

#### 토론

- [스마트 컨트랙트 연구 포럼](https://www.smartcontractresearch.org)

#### 해킹 사건 보고

- [Rekt News](https://rekt.eth.link/leaderboard) - 내부 고발자와 디파이 탐정들이 커뮤니티에 정보를 제공할 수 있는 익명 플랫폼.
- [Blockchain Threat Intelligence](https://blockthreat.substack.com/) - 가상화 환경의 최신 보안 뉴스, 도구, 이벤트, 취약점 및 위협을 다루는 뉴스레터입니다. [이 레포를 지원해주세요.](https://github.com/openblocksec/blocksec-incidents)
- [Blockchain Graveyard](https://magoo.github.io/Blockchain-Graveyard/) - 블록체인과 관련된 대규모 보안 침해와 절도 리스트

# 도구 모음

#### 이더리움 Tools

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

#### 라이브러리

- [dapp-bin](https://github.com/ethereum/dapp-bin) - 이더리움 솔리디티, Serpent 그리고 LLL의 많은 공통 데이터 구조와 유틸리티에 대한 구현을 제공합니다.
- [솔리디티 모음](https://github.com/ethereum/wiki/wiki/Solidity-Collections) - 코드 조각과 유틸리티 라이브러리 모음입니다.
- [OpenZeppelin](https://openzeppelin.org/) - 안전한 스마트 컨트랙트을 구축하기 위한 프레임워크

#### 널리 사용되는 스마트 컨트랙트 라이브러리

- [Zeppelin](https://github.com/OpenZeppelin/openzeppelin-contracts) - SafeMath와 OpenZeppelin SDK 같이 테스트를 거친 재사용 가능한 스마트 컨트랙트이 포함된 [라이브러리](https://github.com/OpenZeppelin/openzeppelin-sdk)
- [cryptofin-solidity](https://github.com/cryptofinlabs/cryptofin-solidity) - 이더리움에서 안전하고 가스 효율적인 스마트 컨트랙트을 구축하기 위한 솔리디티 라이브러리입니다.
- [Modular Libraries](https://github.com/Modular-Network/ethereum-libraries) - 이더리움 가상 머신을 사용하는 블록체인에서 사용하기 위해 만들어진 패키지 그룹
- [DateTime Library](https://github.com/bokkypoobah/BokkyPooBahsDateTimeLibrary) - 가스 효율적인 솔리디티 날짜와 시간 라이브러리
- [Aragon](https://github.com/aragon/aragon) - DAO 프로토콜. [aragonOS 스마트 컨트랙트 프레임워크](https://github.com/aragon/aragonOS) 업그레이드 가능성을 가진 거버넌스에 중점을 둠
- [ARC](https://github.com/daostack/arc) - DAO 및 DAO 스택의 기본 계층을 위한 운영 체제입니다.
- [0x](https://github.com/0xProject) - DEX 프로토콜
- [Token Libraries with Proofs](https://github.com/sec-bit/tokenlibs-with-proofs) - 지정된 사양과 상위 수준의 속성에 대한 토큰 컨트랙트 wrt의 정확성 증명 포함
- [Provable API](https://github.com/provable-things/ethereum-api) - 오프체인 작업, 데이터 가져오기와 계산을 허용하는 Probable 서비스 사용 컨트랙트을 제공합니다.
- [ABDK Libraries for Solidity](https://github.com/abdk-consulting/abdk-libraries-solidity) - 고정점(64.64비트) 그리고 IEEE-754 호환 4중 정밀도(129비트) 솔리드용 부동 소수점 산술 라이브러리

#### 스마트 컨트랙트 패턴

- [Dappsys: 안전하고 단순하며 유연한 이더리움 컨트랙트 구성 요소](https://github.com/dapphub/dappsys)
- [MakerDAO](https://github.com/makerdao/maker-otc)
- [The TAO](https://github.com/ryepdx/the-tao)
- [Dapp-a-day 1-10](https://steemit.com/@nikolai)
- [Dapp-a-day 11-25](https://steemit.com/@nexusdev)
- [OpenZeppelin Contracts: 재사용 가능하고 안전한 스마트 컨트랙트을 솔리디티 언어로 제공하는 개발형 프레임워크](https://github.com/OpenZeppelin/openzeppelin-contracts)
- [보안 감사 모범 사례에 대한 블로그](https://blog.openzeppelin.com/)
- [어셈블리 포함 고급 작업장](https://github.com/androlo/solidity-workshop)
- [더 단순한 이더리움 Multisig](https://medium.com/@ChrisLundkvist/exploring-simpler-ethereum-multisig-contracts-b71020c19037) - 특히 _benefits_ 섹션
- [CryptoFin 솔리디티 회계 감사 체크리스트](https://github.com/cryptofinlabs/audit-checklist) - 메인넷 론칭 컨트랙트을 감사할 때 주의해야할 공통 소견 및 문제의 체크리스트입니다.
- [aragonOS: A smart contract framework for building DAOs, Dapps and protocols](https://hack.aragon.org/docs/aragonos-intro.html)

#### 업그레이드 가능성

- [블로그 von Elena Dimitrova, Dev at colony.io](https://blog.colony.io/author/elena/)
- [라이브러리 기반 개발](https://blog.aragon.org/library-driven-development-in-solidity-2bebcaf88736)
- [고급 솔리디티 코드 배포 기술](https://blog.aragon.org/advanced-solidity-code-deployment-techniques-dc032665f434/)
- [OpenZeppelin의 프록시 라이브러리](https://blog.openzeppelin.com/proxy-libraries-in-solidity-79fbe4b970fd/)

#### 개발 도구

- [CryptoFin 솔리디티 회계 감사 체크리스트](https://github.com/cryptofinlabs/audit-checklist) - 메인넷 론칭 컨트랙트을 감사할 때 주의해야 할 공통 소견 및 문제 체크리스트입니다.
- [MythX](https://mythx.io/) - 이더리움 개발자를 위한 보안 검증 플랫폼과 생태계
- [Mythril](https://github.com/ConsenSys/mythril) - 오픈소스 EVM 바이트 코드 보안 분석 도구
- [Oyente](https://github.com/melonproject/oyente) - 대체 정적 스마트 컨트랙트 보안 분석
- [Securify](https://securify.chainsecurity.com/) - 이더리움 스마트 컨트랙트용 보안 스캐너
- [SmartCheck](https://tool.smartdec.net/) - 정적 스마트 컨트랙트 보안 분석기
- [Ethersplay](https://github.com/crytic/ethersplay) - EVM 분해기
- [Evmdis](https://github.com/Arachnid/evmdis) - 대체 EVM 분해기
- [Hydra](https://github.com/IC3Hydra/Hydra) - 암호화 경제 컨트랙트 보안 프레임워크, 분산된 보안 보조금
- [Solgraph](https://github.com/raineorshine/solgraph) - 스마트 컨트랙트 보안 분석을 위한 솔리디티 제어 흐름 시각화
- [Manticore](https://github.com/trailofbits/manticore) - 스마트 컨트랙트과 이진 파일에 대한 심볼 실행ㅇ 도구
- [Slither](https://github.com/crytic/slither) - 솔리디티 정적 분석 프레임워크
- [Adelaide](https://github.com/sec-bit/adelaide) - SECBIT 정적 분석 기능을 솔리티 컴파일러로 확장
- [solc-verify](https://github.com/SRI-CSL/solidity/) - 솔리디티 스마트 컨트랙트에 대한 모듈식 검증자
- [솔리디티 보안 블로그](https://github.com/sigp/solidity-security-blog) - 알려진 공격 벡터와 일반적인 안티패턴의 포괄적인 목록
- [Awesome Buggy ERC20 Tokens](https://github.com/sec-bit/awesome-buggy-erc20-tokens) - 영향을 받는 토큰과 ERC20 스마트 컨트랙트에서 취약성 모음
- [Free Smart Contract Security Audit](https://callisto.network/smart-contract-audit/) - Callisto에서 Network로의 무료 스마트 컨트랙트 보안 감사
- [Piet](https://piet.slock.it) - 시각적 솔리디티 아키텍처 분석기

#### 프론트엔드 이더리움 APIs

- [Web3.js](https://github.com/ethereum/web3.js/) - 자바스크립트 Web3
- [Eth.js](https://github.com/ethjs) - 자바스크립트 Web3 대안
- [Ethers.js](https://github.com/ethers-io/ethers.js/) - 자바스크립트 Web3 대안, 유용한 유틸리티와 지갑 기능
- [light.js](https://github.com/paritytech/js-libs/tree/master/packages/light.js) - 경량 클라이언트에 최적화된 높은 수준의 사후 대응형 JS 라이브러리
- [Web3Wrapper](https://github.com/0xProject/0x-monorepo/tree/development/packages/web3-wrapper) - 타입스크립트 Web3 대안
- [Ethereumjs](https://github.com/ethereumjs/) - 이더리움 같은 유틸리티 기능 모음 [ethereumjs-util](https://github.com/ethereumjs/ethereumjs-util) 그리고 [ethereumjs-tx](https://github.com/ethereumjs/ethereumjs-tx)
- [Alchemy-web3.js](https://github.com/alchemyplatform/alchemy-web3) - 자동 재시도를 포함한 자바스크립트 Web3 wrappers, access to [Alchemy's enhanced APIs](https://docs.alchemyapi.io/documentation/alchemy-web3/enhanced-web3-api), 그리고 강력한 웹 소켓 연결.
- [flex-contract](https://github.com/merklejerk/flex-contract) 그리고 [flex-ether](https://github.com/merklejerk/flex-ether) - 스마트 컨트랙트과 상호 작용하고 트랜잭션을 수행할 수 있는 최신 제로 구성 고급 라이브러리
- [ez-ens](https://github.com/merklejerk/ez-ens) - 간단한 제로 구성 이더리움 이름 서비스 주소 확인 도구입니다.
- [web3x](https://github.com/xf00f/web3x) - web3.js의 타입스크립트 포트. 편익에는 컨트랙트과 상호작용하는 경우를 포함하여 소규모 빌드와 전체 유형 안전이 포함됩니다.
- [Nethereum](https://github.com/Nethereum/) - 크로스 플랫폼 이더리움 개발 프레임워크
- [dfuse](https://github.com/dfuse-io/client-js) - [dfuse Ethereum API](https://dfuse.io)를 사용하는 타입스크립트 라이브러리
- [Drizzle](https://github.com/truffle-box/drizzle-box) - 프론트 엔드를 블록체인에 연결하는 리덕스 라이브러리
- [Tasit SDK](https://github.com/tasitlabs/tasitsdk) - 리액트 네이티브를 이용한 네이티브 모바일 이더리움 기본앱 제작 자바스크립트 SDK
- [useMetamask](https://github.com/mdtanrikulu/use-metamask) - 이더리움에서 메타마스크를 관리하기 위한 맞춤형 리액트 Hook
- [WalletConnect](https://walletconnect.org/) - Dapp에 지갑 연결을 위한 개방형 프로토콜
- [Subproviders](https://0x.org/docs/tools/subproviders) - [Web3-provider-engine](https://github.com/MetaMask/web3-provider-engine)(dApp에 레저 하드웨어 지갑 지원을 추가하기 위한 레저 Subprovider 포함)과 함께 사용할 수 있는 몇 가지 유용한 하위 공급업체
- [ethvtx](https://github.com/ticket721/ethvtx) - ethereum-ready & framework-agnostic 리덕스 저장소 구성 [docs](https://ticket721.github.io/ethvtx/)
- Strictly Typed - 자바스크립트 대안
- [elm-ethereum](https://github.com/cmditch/elm-ethereum)
- [purescript-web3](https://github.com/f-o-a-m/purescript-web3)
- [ChainAbstractionLayer](https://github.com/liquality/chainabstractionlayer) - 단일 인터페이스를 사용하여 서로 다른 블록체인(이더리움 포함)과 통신합니다.
- [Delphereum](https://github.com/svanas/delphereum) - Windows, MacOS, iOS, Android용 네이티브 dApp 개발을 가능하게 하는 이더리움 블록체인에 대한 델파이 인터페이스.
- [Torus](https://tor.us/) - 원할한 온보드 UX로 애플리케이션을 구축하기 위한 오픈 소스 SDK
- [Fortmatic](https://fortmatic.com/) - SDK를 사용하여 확장과 다운로드 없이 web3 dApp을 쉽게 구축할 수 있습니다.
- [Portis](https://portis.io/) - 아무것도 설치하지 않고도 DAP와 쉽게 상호 작용할 수 있는 SDK가 포함된 비 커스터디 지갑입니다.
- [create-eth-app](https://github.com/paulrberg/create-eth-app) - 한 번의 명령으로 이더리움 작동 프런트-엔드 앱을 만들 수 있습니다.
- [Scaffold-ETH](https://github.com/austintgriffith/scaffold-eth) - 스마트 컨트랙트 구축을 위한 초보자 친화적인 포크 허브
- [Notify.js](https://blocknative.com/notify) - 사용자에게 실시간 알림 제공 Blocknative Notify.js는 속도 증가와 취소에 대한 내장 지원을 통해 사용자가 안심하고 거래할 수 있도록 지원합니다. Notify.js는 통합이 쉽고 사용자 지정이 빠릅니다.

#### 백엔드 이더리움 APIs

- [Web3.py](https://github.com/ethereum/web3.py) - 파이썬 Web3
- [Web3.php](https://github.com/sc0Vu/web3.php) - PHP Web3
- [Ethereum-php](https://github.com/digitaldonkey/ethereum-php) - PHP Web3
- [Web3j](https://github.com/web3j/web3j) - 자바 Web3
- [Nethereum](https://nethereum.com/) - .Net Web3
- [Ethereum.rb](https://github.com/EthWorks/ethereum.rb) - 루비 Web3
- [rust-web3](https://github.com/tomusdrw/rust-web3) - 러스트 Web3
- [ethers-rs](https://github.com/gakonst/ethers-rs/) - Ethers-rs
- [Web3.hs](https://hackage.haskell.org/package/web3) - 하스켈 Web3
- [KEthereum](https://github.com/komputing/KEthereum) - 코틀린 Web3
- [Eventeum](https://github.com/ConsenSys/eventeum) - Kauri가 자바로 작성한 이더리움 스마트 컨트랙트 이벤트와 백엔드 마이크로서비스의 연결고리
- [Ethereumex](https://github.com/mana-ethereum/ethereumex) - Elixir JSON-RPC 클라이언트를 위한 이더리움 블록체인
- [Ethereum-jsonrpc-gateway](https://github.com/HydroProtocol/ethereum-jsonrpc-gateway) - 다중화와 로드 밸런싱을 위해 여러 이더리움 노드를 실행할 수 있는 게이트웨이입니다. Infura의 대안으로 실행할 수 있습니다. Golang으로 작성되어 있습니다.
- [EthContract](https://github.com/AgileAlpha/eth_contract) - Elixir에서 이더리움 스마트 컨트랙트을 쿼리하는데 도움이 되는 일련의 helper 메소드들
- [Ethereum Contract Service](https://github.com/mesg-foundation/service-ethereum-contract) - 주소 및 ABI에 따라 모든 이더리움 컨트랙트과 상호 작용할 수 있는 서비스.
- [Ethereum Service](https://github.com/mesg-foundation/service-ethereum) - 이더리움의 이벤트와 상호 작용하고 상호 작용할 수 있는 MESG 서비스입니다.
- [Marmo](https://marmo.io/) - 파이썬, 자바스크립트, 자바 SDK로 이더리움과 상호 작용을 단순화합니다. 릴레이를 사용하여 트랜잭션 비용을 릴레이로 오프로드합니다.
- [이더리움 로그 프레임워크](https://bitbucket.csiro.au/users/kli039/repos/ethereum-logging-framework/browse) - 쿼리 언어, 쿼리 프로세서, 로깅 코드 생성을 포함한 이더리움 애플리케이션 및 네트워크의 고급 로깅 기능 제공

#### 이더리움 클라이언트들

- [Besu](https://besu.hyperledger.org/en/latest/) - Apache 2.0 라이센스에 따라 개발되고 자바로 작성된 오픈 소스 이더리움 클라이언트로 하이퍼레저가 호스팅합니다.
- [Geth](https://geth.ethereum.org/docs/) - Go 클라이언트.
- [Erigon](https://github.com/ledgerwatch/erigon) - 효율성 프론티어 기반으로 하는 이더리움 클라이언트의 대부분 Go 구현
- [OpenEthereum](https://github.com/openethereum/openethereum) - 이전에는 Parity라고 불렸던 러스트 클라이언트. Erigon에게 유리한 비난의 길
- [Aleth](https://github.com/ethereum/aleth) - C++ 클라이언트
- [Nethermind](https://github.com/NethermindEth/nethermind) - .NET Core 클라이언트
- [Infura](https://infura.io/) - 이더리움 클라이언트 표준 호환 API를 제공하는 관리형 서비스
- [Trinity](https://trinity.ethereum.org/) - [py-evm](https://github.com/ethereum/py-evm)을 사용하는 파이썬 클라이언트
- [Ethereumjs](https://github.com/ethereumjs/ethereumjs-client) - [ethereumjs-vm](https://github.com/ethereumjs/ethereumjs-vm)을 사용하는 자바스크립트 클라이언트
- [Seth](https://github.com/dapphub/dapptools/tree/master/src/seth) - Seth는 "명령줄용 메타마스크" 같은 이더리움 클라이언트 도구입니다.
- [Mustekala](https://github.com/musteka-la/mustekala) - 메타마스크의 이더리움 라이트 클라이언트 프로젝트
- [Exthereum](https://github.com/exthereum/blockchain) - Elixir 클라이언트
- [EWF Parity](https://github.com/energywebfoundation/energyweb-ui) - Tobalaba 테스트 네트워크를 위한 Energy Web Foundation 클라이언트
- [Quorum](https://github.com/jpmorganchase/quorum) - [JP Morgan](https://jpmorgan.com/quorum)에 의해 데이터 프라이버시를 지원하는 이더리움의 허용 구현
- [Mana](https://github.com/mana-ethereum/mana) - Elixir로 작성된 이더리움 전체 노드 구현.
- [Chainstack](https://chainstack.com/) - 전용 공유 Geth 노드를 제공하는 관리형 서비스
- [QuikNode](https://quiknode.io/) - API 엑세스 및 서비스형 노드(node-as-a-aservice)를 지원하는 블록쳉인 개발자 클라우드입니다.

#### 저장소

- [IPFS](https://ipfs.io/) - 분산된 스토리지 및 파일 참조
- [Mahuta](https://github.com/ConsenSys/Mahuta) - 검색 기능이 추가된 IPFS 스토리지 서비스 (이전으이 IPFS-스토어)
- [OrbitDB](https://github.com/orbitdb/orbit-db) - IPFS를 기반으로 분산된 데이터 베이스
- [JS IPFS API](https://github.com/ipfs/js-ipfs-http-client) - 자바스크립트에 구현된 IPFS HTTP API용 클라이언트 라이브러리
- [TEMPORAL](https://github.com/RTradeLtd/Temporal) - IPFS와 기타 분산/중앙 집중식 스토리지 프로토콜로 사용하기 쉬운 API
- [PINATA](https://pinata.cloud) - IPFS를 사용하는 가장 쉬운 방법
- [Swarm](https://swarm-gateways.net/) - 이더리움 web3 스택의 네이트 기본 계층 서비스인 분산 스토리지 플랫폼과 콘텐츠 배포 서비스
- [Infura](https://infura.io/) - 관리되는 IPFS API 게이트웨이 및 고정 서비스
- [3Box Storage](https://docs.3box.io/api/storage) - 사용자가 제어하고 분산된 스토리지를 위한 API입니다. IPFS와 Orbitdb위에 구축됩니다.
- [Aleph.im](https://aleph.im/) - 이더리움과 IPFS와 호환되는 오프체인 인센티브 P2P(Peer-to-Peer) 클라우드 프로젝트 (데이터베이스, 파일 스토리지, 컴퓨팅과 DID)

#### 부트스트랩/기본 제공 도구

- [Truffle boxes](https://trufflesuite.com/boxes) - 이더리움 에코시스템을 위한 패키지 구성 요소
- [Create Eth App](https://github.com/paulrberg/create-eth-app) - 한 번의 명령으로 이더리움 기반 프론트 엔드 앱 생성
- [Besu Private Network](https://besu.hyperledger.org/en/stable/Tutorials/Quickstarts/Azure-Private-Network-Quickstart/) - 도커 컨테이너에서 Besu 노드의 전용 네트워크 실행
- [Testchains](https://github.com/Nethereum/TestChains) - 사전 구성된 신속한 대응을 위한 .NET 개발(PoA)
- [Blazor/Blockchain Explorer](https://github.com/Nethereum/NethereumBlazor) - WASM 블록체인 탐색기(기능 샘플)
- [Local Raiden](https://github.com/ConsenSys/Local-Raiden) - 데모와 테스트를 위해 도커 컨테이너에서 로컬 Raiden 네트워크 실행
- [Private networks deployment scripts](https://github.com/ConsenSys/private-networks-deployment-scripts) - 프라이빗 PoA 네트워크를 위한 기본 제공 배포 스크립트
- [Parity Demo-PoA Tutorial](https://wiki.parity.io/Demo-PoA-tutorial.html) - Parity 권한을 가진 2개의 노드로 구성된 PoA 테스트 체인을 구축하기 위한 단계별 튜토리얼 전반적 합의
- [Local Ethereum Network](https://github.com/ConsenSys/local_ethereum_network) - 프라이빗 PoW 네트워크를 위한 기본 제공 배포 스크립트
- [Kaleido](https://kaleido.io/) - Caleido를 사용하여 협력단 블록체인 네트워크를 구축합니다. PoC와 테스트에 적합합니다.
- [Cheshire](https://github.com/endless-nameless-inc/cheshire) - A local sandbox implementation of the CryptoKitties API and smart contracts, available as a Truffle Box
- [aragonCLI](https://github.com/aragon/aragon-cli) - aragonCLI 아라곤 애플리케이션 및 조직을 만들고 개발하는데 사용됩니다.
- [ColonyJS](https://github.com/JoinColony/colonyJS) - Conlony 네트워크 스마트 컨트랙트과 상호 작용할 수 있는 API를 제공하는 자바스크립트 클라이언트입니다.
- [ArcJS](https://github.com/daostack/arc.js) - DAOstack Arc 이더리움 스마트 컨트랙트에 대한 자바스크립트 애플리케이션 액세스를 용이하게 하는 라이브러리입니다.
- [Arkane Connect](https://docs.arkane.network/pages/connect-js.html) - 사용자 친화적인 앱을 구축하기 위한 지갑 공급업체인 Arkane Network와 상호 작용할 수 있는 API를 제공하는 자바스크립트 클라이언트입니다.
- [Onboard.js](https://blocknative.com/onboard) - 블록 네이티브 온보드는 프로젝트에 멀티 지갑 지원을 빠르고 쉽게 추가할 수 있는 방법입니다. 20개 이상의 고유한 하드웨어와 소프트웨어 지갑에 사용할 수 있는 내장 모듈을 통해 시간과 번거로움을 줄일 수 있습니다.
- [web3-react](https://github.com/NoahZinsmeister/web3-react) - 싱글 페이지 이더리움 dApp 구축을 위한 리액트 프레임워크

#### 이더리움 ABI (Application Binary Interface) 도구

- [ABI decoder](https://github.com/ConsenSys/abi-decoder) - 이더리움 트랜잭션에서 데이터 매개 변수와 이벤트 디코딩하는 라이브러리
- [ABI-gen](https://github.com/0xProject/0x-monorepo/tree/development/packages/abi-gen) - 컨트랙트 ABI에서 타입스크립트 컨트랙트 래퍼 생성
- [Ethereum ABI UI](https://github.com/hiddentao/ethereum-abi-ui) - 이더리움 컨트랙트 ABI에서 UI 양식 필드 정의와 관련 검증자 자동생성
- [headlong](https://github.com/esaulpaugh/headlong/) - 타입-세이프 컨트랙트 ABI 및 자바 재귀 길이 접두사 라이브러리
- [EasyDapper](https://www.easydapper.com) - Truffle 아티팩트에서 생성된 애플리케이션, 공용/비공개 네트워크에 컨트랙트 배포, 컨트랙트과 상호 작용할 수 있는 사용자 지정 가능한 실시간 공개 페이지 제공
- [One Click dApp](https://oneclickdapp.com) - ABI를 사용하여 고유한 URL에서 즉시 dApp을 생성합니다.
- [Truffle Pig](https://npmjs.com/package/trufflepig) - Truffle에서 생성된 컨트랙트 파일을 찾아 읽을 수 있는 간단한 HTTP AP를 제공하는 개발도구입니다. http를 통해 새 컨트랙트 ABI를 제공합니다.
- [Ethereum Contract Service](https://github.com/mesg-foundation/service-ethereum-contract) - 주소와 ABI를 기반으로 이더리움 컨트랙트과 상호 작용할 수 있는 MESG 서비스.
- [Nethereum-CodeGenerator](https://github.com/StefH/Nethereum-CodeGenerator) - 솔리디티 스마트 컨트랙트을 기반으로 Netheum 기반 C# 인터페이스와 서비스를 생성하는 웹 기반 생성기.

# 테스트 도구

- [Truffle Teams](https://trufflesuite.com/teams) - 구성이 필요 없는 Truffle 프로젝트를 위한 지속적인 통합
- [Solidity code coverage](https://github.com/0xProject/0x-monorepo/tree/development/packages/sol-coverage) - 솔리디티 코드 커버리지 툴
- [Solidity coverage](https://github.com/sc-forks/solidity-coverage) - 솔리디티 스마트 컨트랙트을 위한 대체 코드 커버리지
- [Solidity function profiler](https://github.com/EricR/sol-function-profiler) - 솔리디티 컨트랙트 함수 프로파일러
- [Sol-profiler](https://github.com/Aniket-Engg/sol-profiler) - 솔리디티 컨트랙트 함수 프로파일러 대안
- [Espresso](https://github.com/hillstreetlabs/espresso) - 빠르고 병렬화된 핫 리로드 솔리드 테스트 프레임워크
- [Eth tester](https://github.com/ethereum/eth-tester) - 이더리움 애플리케이션 테스트를 위한 툴 제품군
- [Cliquebait](https://github.com/f-o-a-m/cliquebait) - 실제 블록체인 네트워크와 매우 유사한 도커 인스턴스를 통해 스마트 컨트랙트 애플리케이션의 통합 테스트 수용 간소화
- [Hevm](https://github.com/dapphub/dapptools/tree/master/src/hevm) - hevm 프로젝트는 유닛 테스트 및 스마트 컨트랙트 디버깅을 위해 특별히 만들어진 이더리움 가상 머신(EVM)을 구현한 것입니다.
- [Ethereum graph debugger](https://github.com/fergarrui/ethereum-graph-debugger) - 솔리디티 그래픽 디버거
- [Tenderly CLI](https://github.com/Tenderly/tenderly-cli) - 사람이 판독할 수 있는 스택 추적을 통해 개발 가속화
- [Solhint](https://github.com/protofire/solhint) - 스마트 컨트랙트 검증을 위한 보안, 스타일 가이드와 모범 사례 규칙을 제공하는 솔리디티 라이터
- [Ethlint](https://github.com/duaraghav8/Ethlint) - 솔리디티, 이전의 Solium에서 스타일 그리고 보안 문제를 식별하고 해결하기 위한 린터
- [Decode](https://github.com/hacker-DOM/decode) - 로컬 testrpc 노드에 제출된 tx를 보다 읽기 쉽고 이해하기 쉽게 구문 분석하는 npm 패키지
- [truffle-assertions](https://github.com/rkalis/truffle-assertions) - 솔리디티 스마트 컨트랙트을 Truffle와 테스트하는데 사용되는 추가 주장 그리고 효용과과 함께 npm 패키지.
  중요한 점. 특정 사건이 발생했는지 여부를 주장할 수 있는 능력을 추가합니다.
- [Psol](https://github.com/Lamarkaz/psol) - mustache.js 스타일구문, 매크로, 조건부 컴파일과 자동 원격 종속성이 포함된 솔리디티 어휘 사전 프로세서.
- [solpp](https://github.com/merklejerk/solpp) - 종합적인 지시어와 표현 언어, 고정밀 산순과많은 유용한 helper 기능을 갖춘 솔리디티 전처리기 그리고 평탄기
- [Decode and Publish](https://flightwallet.github.io/decode-eth-tx/) – 원시 이더리움 tx를 코딩하여 게시하며 https://live.blockcypher.com/btc-testnet/decodetx/ 유사합니다.
- [Doppelgänger](https://getdoppelganger.io/) - 유닛 테스트 중 스마트 컨트랙트 의존성을 목킹하는 라이브러리
- [rocketh](https://github.com/wighawag/rocketh) - 원하는 web3 라이브러리와 테스트 러너를 사용할 수 있는 간단한 라이브러리. 이더리움 스마트 컨트랙트을 테스트합니다.
- [pytest-cobra](https://github.com/cobraframework/pytest-cobra) - 이더리움 블록체인 스마트 컨트랙트 테스트를 위한 PyTest 플러그인

#### 트랜잭션 시각화, 득점과 추적:

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

## 프로젝트를 지원해주세요.

프로젝트를 지원하는 것은 매우 중요합니다.
덕분에 직장에서 보내는 시간을 줄이고 제가 좋아하는 일인 디파이와 암호화폐 교육을 할 수 있습니다. :sparkling_heart:

지원하고 싶다면 다음주소로 기부금을 보내주시면 됩니다.

**0xB25C5E8fA1E53eEb9bE3421C59F6A66B786ED77A** — ERC20 & ETH

**17Ydx9m7vrhnx4XjZPuGPMqrhw3sDviNTU** - BTC

## 한글화 날짜

2021.07.05

(👍 ͡❛ ͜ʖ ͡❛)👍
