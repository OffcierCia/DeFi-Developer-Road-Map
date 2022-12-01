# DeFi 开发者路线图

**此库收集了最好的 DeFi 和区块链的研究技术和一些工具, 你也可以在此进行讨论—— 欢迎贡献你的想法**

**在此, 你可以随意提交 pull request，小到修复, 大到翻译、文档或添加任何你想要的工具，应有尽有。**

[![Support Project](https://img.shields.io/badge/Support-Project-critical)](https://github.com/OffcierCia/DeFi-Developer-Road-Map#support-project) [![Supported by GitCoin](https://img.shields.io/badge/Support%20via-GitCoin-yellowgreen)](https://gitcoin.co/grants/3150/defi-developer-roadmap) [![Supported by LEGO](https://img.shields.io/badge/Supported%20by-LEGO-%2300A3FF)](https://www.notion.so/LEGO-Lido-Ecosystem-Grants-Organisation-d7f0bf0182d44348b6173639d2e8363d) 
  [![Research Base](https://img.shields.io/badge/Research-Base-lightgrey )](https://github.com/OffcierCia/ultimate-defi-research-base)
       [![Mail](https://img.shields.io/badge/Mail-offcierciapr%40protonmail.com-brightgreen)](mailto:offcierciapr@protonmail.com) 



<details>
<summary>其他语言</summary>
<br />
- [法语](https://github.com/OffcierCia/DeFi-Developer-Road-Map/blob/main/translations/README_fr.md)
- [古吉拉特语](https://github.com/OffcierCia/DeFi-Developer-Road-Map/blob/main/translations/README_guj.md)

- [韩语](https://github.com/OffcierCia/DeFi-Developer-Road-Map/blob/main/translations/README_ko.md)
- [意大利语](https://github.com/OffcierCia/DeFi-Developer-Road-Map/blob/main/translations/README_it.md)

</details>


## 路线图

![Roadmap](../DeFiRoadMapNewSVG.svg)

# 导航


|      主题      | 链接                                        |
| :------------: | ------------------------------------------- |
|      基础      | [点击查看](#基础)                           |
|     dApps      | [点击查看](#dApps)                          |
|      框架      | [点击查看](#框架)                           |
|   zk-snarks    | [点击查看](#ZK-SNARKs)                      |
|    更多阅读    | [点击查看](#更多阅读)                       |
|   安全与保障   | [点击查看](#安全与保障)                     |
|      DeFi      | [点击查看](#DeFI)                           |
| 以太坊域名服务 | [点击查看](#以太坊域名服务)                 |
|      NFT       | [点击查看](#非同质化代币 (NFT))             |
|     稳定币     | [点击查看](#稳定币)                         |
|    其它资料    | [点击查看](#其它资料)                       |
|      支链      | [点击查看](#支链)                           |
| 矿工可提取价值 | [点击查看](#最大可提取价值//矿工可提取价值) |
|    工具合集    | [点击查看](#工具合集)                       |
|   以太坊 2.0   | [点击查看](#以太坊 2.0)                     |
|      前端      | [点击查看](#前端)                           |
|    项目管理    | [点击查看](#项目管理)                       |

**| 作者注：**

- [我在 Mirror 上的博客](https://officercia.mirror.xyz/UpFfG7-1E4SDJttnmuQ7v4BMc4KrCXzo80vtx7qV-YY)
- [我在 HackerNoon 上的博客](https://hackernoon.com/u/officercia)
- [所有已知的智能合约端和用户端的攻击与攻击向量](https://graph.org/All-known-smart-contract-side-and-user-side-attacks-and-vulnerabilities-in-Web30--DeFi-03-31)
- [存储加密冷钱包攻击防御方法最佳实践的关键原则](https://hackernoon.com/whats-the-safest-way-to-store-crypto)
- [全方位的 NFT 安全性](https://graph.org/NFT-security-01-28)
- [现有的所有 ETH 安全工具](https://graph.org/ETHSec-Tools-02-13)
- [所有优秀的 TG Dev 社区 ](https://graph.org/Crypto-Telegram-Channels--Chats-04-19)
- [Solidity 语言备忘单、工具和参考资料合集](https://graph.org/Solidity-Cheatsheets-Pack-03-20)

# 基础:


- 学习分布式账本技术（DLT）的基础知识
- 比特币协议 [解释](https://medium.com/coinmonks/bitcoin-white-paper-explained-part-1-4-16cba783146a)
- 椭圆曲线[密码学](https://medium.com/coinmonks/learn-how-to-code-elliptic-curve-cryptography-a952dfdc20ab)
- 阅读 [区块链解释](https://www.investopedia.com/terms/b/blockchain.asp)
- 观看 [区块链 —— 视觉演示](https://www.youtube.com/watch?v=_160oMzblY8)
- 观看 [【官方双语】想知道比特币（和其他加密货币）的原理吗？](https://www.bilibili.com/video/BV11x411i72w)
- 观看 [But how does bitcoin actually work? - 3b1b](https://www.youtube.com/watch?v=bBC-nXj3Ng4) (此行是上行的英文版本)
- 学习 [计算机科学基础](https://github.com/ossu/computer-science)

#### 以太坊 (Ethereum)

- 以太坊基础
- 以太坊虚拟机 (EVM): 图灵完备
- 学习以太坊钱包, 账户 (EOA), 私钥/公钥
- 学习交易, Gas, 小狐狸 (Metamask)
- 以太坊节点和客户端, Geth
- Infura 基础设施

#### 智能合约 (Smart Contract)


- 智能合约基础
- 智能合约的生命周期
- 以太坊高级语言（**Solidity**、Vyper、LLL、Serpent）
- 编译、测试、部署智能合约
- 使用 web3.js 或 web3.py 与智能合约交互
- 阅读[以太坊是如何工作的？](https://www.preethikasireddy.com/post/how-does-ethereum-work-anyway#:~:text=The%20Ethereum%20blockchain%20uses%20an,tokens%20are%20generated%20and%20awarded.)
- 阅读[这篇](https://blog.zeppelin.solutions/the-hitchhikers-guide-to-smart-contracts-in-ethereum-848f08001f05)
- 阅读 [Truffle 文档](https://truffleframework.com/docs/) / [Hardhat 文档](https://hardhat.org/getting-started/)
- 阅读 [Web3 文档](https://web3js.readthedocs.io/en/1.0/) / [Ethers 文档](https://docs.ethers.io/v5/)
- 阅读书籍[《精通以太坊》](https://github.com/ethereumbook/ethereumbook) 还有观看[这个频道](https://www.youtube.com/channel/UCJWh7F3AFyQ_x01VKzr9eyA/videos)
- 阅读 [Solidity 智能合约库](https://openzeppelin.org/api/docs/get-started.html) and [Solidity 基础](https://solidity-by-example.org)（教程来自 Zombies）](https://cryptozombies.io)
- 阅读[去中心化金融中现金网络威胁的闪崩](https://arxiv.org/pdf/2106.10740.pdf)

#### 智能合约标准

- [ERCs](https://eips.ethereum.org/erc) - 以太坊改进提议（EIPs）

#### 代币(Tokens)

- [ERC-20](https://eips.ethereum.org/EIPS/eip-20) - 同质化代币标准
- [ERC-721](https://github.com/ethereum/eips/issues/721) - 非同质化代币标准
- [ERC-1155](https://eips.ethereum.org/EIPS/eip-1155) - 半同质化代币标准
- [ERC-918](https://eips.ethereum.org/EIPS/eip-918) - 可开采代币标准
- [代币交互清单](https://consensys.net/diligence/blog/2020/11/token-interaction-checklist/)

#### Others

- [ERC-165](https://eips.ethereum.org/EIPS/eip-165) - 标准接口检测
- [ERC-725](https://eips.ethereum.org/EIPS/eip-725) - 以太坊身份标准
- [ERC-173](https://eips.ethereum.org/EIPS/eip-173) - 合同所有权标准


#### 通用开发技能


- 学习 [GIT](https://medium.com/pixel-pioneers/the-basics-of-version-control-system-git-explained-by-designing-a-new-car-3fb3a10e9e40)
- 在 [GitHub](https://github.com/) / [GitLab](https://about.gitlab.com/) 上创建一个库
- 与其他人共享您的代码
- 了解 HTTP(S) 协议、请求方法（GET、POST、PUT、PATCH、DELETE、OPTIONS）
- [使用 Google 进行强力搜索](http://www.powersearchingwithgoogle.com/)
- 熟悉终端（[Linux/Docker](https://medium.com/coinmonks/how-to-become-a-blockchain-developer-59c830e20f15)），配置你的 shell（bash、zsh、fish）
- 读几本关于算法和数据结构、区块链、以太坊、solidity 的书
- 完成本课程 [以太坊和 Solidity：完整的开发者指南](https://www.udemy.com/ethereum-and-solidity-the-complete-developers-guide/)
- 免费教程[学习 Solidity](https://github.com/willitscale/learning-solidity)
- [使用 Solidity 开发智能合约简介](https://www.youtube.com/playlist?list=PLV1JDFUtrXpGvu8QHL9b78WYNSJsYNZsb) 和 [ERC20 编程](https://www.youtube.com/watch?v=Hqx5yuskmRU&list=PLYSZ- f9LCH3sEf0UKTLCaZErJeQtK7GCD)
- [Tudelft Repo](https://repository.tudelft.nl)

#### 尝试以下工具:

- [eth-cli](https://github.com/protofire/eth-cli) - 命令行工具。
- [REPL](https://github.com/raineorshine/solidity-repl) - Solidity REPL.
- [Remix](https://remix.ethereum.org/) - 在线实时编译器和运行时。
- [gencall-cli](https://github.com/manifoldfinance/libcaller/tree/master/packages/gencall-cli) - ABI 文件中的交互式智能合约编码器和发送器
- [优化 Solidity 函数名称](https://emn178.github.io/solidity-optimize-name/) - 优化函数名称以降低成本
- [solc-typed-ast compiler](https://github.com/ConsenSys/solc-typed-ast) - TypeScript 包提供规范化的类型化 Solidity AST 以及生成 AST（来自 Solc）和遍历/操作它所需的实用程序。


# dApps

- 熟悉以下工具：

#### 包管理器 (Package Managers)

- [npm](https://www.npmjs.com/)
- [yarn](https://yarnpkg.com/lang/en/)
- [pnpm](https://pnpm.js.org/)

#### IDE's

- [Remix IDE](https://remix.ethereum.org/)
- [Remix IDE Desktop Release](https://github.com/ethereum/remix-desktop/releases)
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
- 在 [VSCode](https://code.visualstudio.com/) 上安装 [Solidity Visual Developer](https://marketplace.visualstudio.com/items?itemName=tintinweb.solidity-visual-auditor) 插件
- [vscode-solidity-lang](https://github.com/contractshark/vscode-solidity-extenstion) Solidity 语法高亮 [VSCode 商店](https://marketplace.visualstudio.com/items?itemName=ContractShark.solidity-lang)
- [MetaMask OpenRCP API Playground](https://metamask.github.io/api-playground/api-documentation/) - 用 MetaMasks RPC API 来查看和辅助交互

 #### Practice

- 通过制作 [僵尸游戏](https://cryptozombies.io/) 来学习以太坊开发。
- 阅读并完成制作此示例: [宠物商店教程](https://www.trufflesuite.com/tutorial)
- [时间锁定钱包：以太坊智能合约简介](https://www.toptal.com/ethereum-smart-contract/time-locked-wallet-truffle-tutorial)
- [终极 ENS 和 ĐApp 教程](https://www.toptal.com/ethereum/ethereum-name-service-dapp-tutorial)
- [以太坊 Ðapp 开发的终极介绍](https://www.youtube.com/playlist?list=PLV1JDFUtrXpFh85G-Ddyy2kLSafaB9biQ)
- [Ethernaut](https://ethernaut.zeppelin.solutions/) 是一款基于 Web3/Solidity 的战争游戏，适合那些对学习以太坊感兴趣的人
- [Ethereum 和 Solidity：完整的开发人员指南](https://www.udemy.com/ethereum-and-solidity-the-complete-developers-guide/)
- [Consensys 最佳实践](https://consensys.github.io/smart-contract-best-practices/) - 本文档为中级 Solidity 程序员提供了安全注意事项的基本知识，由 ConsenSys Diligence 和更广泛的以太坊社区维护。
- [Solidity 模式](https://github.com/fravoll/solidity-patterns) - 模式与最佳实践的整合。
- [智能合约威胁数据库](https://github.com/crytic/not-so-smart-contracts) - 最烂模式的整合。
- [ETH.build](https://eth.build/) 一个针对 Web3 学习的沙箱



# ZK-SNARKs

#### 基本信息

- [zkp.science](https://zkp.science) - 关于 ZK-SNARKs 你应该知道的一切
- [ZoKrates](https://github.com/Zokrates/ZoKrates) - 一个以太坊上关于 zkSNARKS 的工具合集
- [The AZTEC Protocol](https://github.com/AztecProtocol/AZTEC) - 以太坊网络上的加密交易和在以太网主网上实时实施
- [Nightfall](https://github.com/EYBlockchain/nightfall) - 将任何 ERC-20 / ERC-721 代币设为私有 - 开源工具和微服务
- 代理重加密 (PRE)
- [NuCypher Network](https://github.com/nucypher/nucypher) - 代理重加密帮助在去中心化网络中增强数据隐私
- [pyUmbral](https://github.com/nucypher/pyumbral) - 阈值代理重加密密码库
- 全同态加密 (FHE)
- [NuFHE](https://github.com/nucypher/nufhe) - 全同态加密 GPU 加速库

#### ZK-STARKs

- [StarkWare](https://github.com/starkware-industries) 与 [StarkWare 资源](https://github.com/starkware-libs) - StarkEx 可扩展性引擎在链上存储状态转换

# 框架

#### Truffle Suit 

- [Truffle](https://truffleframework.com/truffle)
- [Ganache](https://truffleframework.com/ganache)
- [Drizzle](https://truffleframework.com/drizzle)


#### ZeppelinOS

- [点击这里开始了解](https://docs.zeppelinos.org/docs/start.html)

#### Labs.Superblock

> Note: Superblocks is depreciated

- [Labs.superblocks](https://lab.superblocks.com/)
- [dapp 教程](https://www.youtube.com/watch?v=LK-kVMzrdno)


#### Infura（通往以太坊的网关）

- [主网端点](https://infura.io/)
- [Ropsten 测试网端点](https://infura.io/)
- [Kovan 测试网端点](https://infura.io/)
- [Rinkby 测试网端点](https://infura.io/)
- [星际文件系统](https://medium.freecodecamp.org/hands-on-get-started-with-infura-and-ipfs-on-ethereum-b63635142af0)

#### 其它框架

- [其它框架列表](https://ethereum.org/en/developers/docs/frameworks/)
- [Hardhat](https://hardhat.org/) - 灵活、可扩展和快速的以太坊开发环境。
- [Brownie](https://github.com/iamdefinitelyahuman/brownie) - Brownie 是一个用于部署、测试和与以太坊智能合约交互的 Python 框架。
- [Embark](https://github.com/embark-framework/embark) - DApp 开发框架
- [Waffle](https://getwaffle.io/) - 高级智能合约开发和测试框架，小巧、灵活、快速（基于ethers.js）
- [Dapp](https://dapp.tools/dapp/) - DApp 开发框架，DApple 的后继者
- [Etherlime](https://github.com/LimeChain/etherlime) - 基于 ethers.js 的 Dapp 部署框架
- [Parasol](https://github.com/Lamarkaz/parasol) - [过时] 具有测试、INFURA 部署、自动合约文档等功能的敏捷智能合约开发环境。它具有灵活且不拘一格的设计以及无限的可定制性。
- [0xcert](https://github.com/0xcert/framework/) - 用于构建去中心化应用程序的 JavaScript 框架
- [OpenZeppelin SDK](https://openzeppelin.com/sdk/) - 一套可帮助您开发、编译、升级、部署智能合约并与之交互的工具。
- [sbt-ethereum](https://sbt-ethereum.io/) - 用于智能合约交互和开发的选项卡式基于文本的控制台，包括钱包和 ABI 管理、ENS 支持和高级 Scala 集成。
- [Cobra](https://github.com/cobraframework/cobra) - 一个快速、灵活、简单的以太坊智能合约开发环境框架，在以太坊虚拟机（EVM）上测试和部署。
- [Epirus](https://docs.epirus.io/sdk/) - 用于构建智能合约的 Java 框架。
- [Ether Jar](https://github.com/emeraldpay/etherjar) 以太坊区块链的 Java 集成库
- [Starport](https://github.com/tendermint/starport) - 用于构建支持 IBC 的主权区块链的 CLI 工具。
- [Sign in with Ethereum | SIWE](https://github.com/spruceid/siwe)- 使用消息签名对以太坊帐户进行身份验证的工作流程，以建立一个基于 cookie 的网络会话来管理用户元数据。
- [Foundry](https://github.com/onbjerg/foundry-book) - 一个智能合约开发工具链，用于项目编译、依赖管理、测试、部署、链上交互等。
- [Solmate](https://github.com/Rari-Capital/solmate) - 这些合同已通过审核，但在开发时并未考虑到用户。他们主要寻求优化 gas 和优化智能合约开发。

#### 与智能合约交互

- [Web3.js](https://web3js.readthedocs.io/en/1.0/)
- [Web3.py](https://web3py.readthedocs.io/en/stable/)
- [Web3j](https://docs.web3j.io/latest/)
- [ethers.js](https://docs.ethers.io/v5/)

#### Python 以太坊生态系统

- [阅读文章](https://medium.com/@pipermerriam/the-python-ethereum-ecosystem-101bd9ba4de7)

#### 分布式存储系统

- [点击阅读](https://medium.com/bitfwd/what-is-decentralised-storage-ipfs-filecoin-sia-storj-swarm-5509e476995f)
- [星际文件系统](https://ipfs.io/)
- [MESON](https://meson.network/)
- [SWARM](https://swarm-gateways.net/)
- [Storej](https://storj.io/)
- [Sia](https://sia.tech/)

#### 测试区块链网络

- [Paradigm Faucet](https://faucet.paradigm.xyz) - 在这里领取测试网 ETH
- [Ethnode](https://github.com/vrde/ethnode) - 运行以太坊节点（Geth 或 Parity）进行开发，就像 `npm i -g ethnode && ethnode`.
- [Ganache](https://github.com/trufflesuite/ganache) - 具有可视化用户界面和日志的测试以太坊区块链的应用程序
- [Kaleido](https://kaleido.io/) - 使用 Kaleido 启动联盟区块链网络。非常适合 PoC 和测试
- [Besu 私有网络](https://besu.hyperledger.org/en/stable/Tutorials/Quickstarts/Azure-Private-Network-Quickstart/) - 在 Docker 容器中运行 Besu 节点的私有网络
- [Orion](https://github.com/PegaSysEng/orion) - 通过 PegaSys 执行私人交易的组件
- [Artemis](https://github.com/PegaSysEng/artemis) - PegaSys 对以太坊 2.0 信标链的 Java 实现
- [Cliquebait](https://github.com/f-o-a-m/cliquebait) - 简化智能合约应用程序的集成并能接受测试的 docker 实例，使用起来非常类似于真实的区块链网络
- [Local Raiden](https://github.com/ConsenSys/Local-Raiden) - 在 docker 容器中运行本地 Raiden 网络用于演示和测试目的
- [Private networks deployment scripts](https://github.com/ConsenSys/private-networks-deployment-scripts) - 针对私有 PoA 网络的开箱即用的部署脚本
- [Local Ethereum Network](https://github.com/ConsenSys/local_ethereum_network) - 针对私有 PoW 网络的开箱即用的部署脚本
- [Ethereum on Azure](https://docs.microsoft.com/en-us/azure/blockchain/templates/ethereum-poa-deployment) - 联盟以太坊 PoA 网络的部署和治理
- [Ethereum on Google Cloud](https://console.cloud.google.com/marketplace/details/click-to-deploy-images/ethereum?filter=category:developer-tools) - 基于工作量证明构建以太坊网络
- [Infura](https://infura.io/) - 以太坊 API 访问以太坊网络（Mainnet、Ropsten、Rinkeby、Goerli、Kovan）
- [CloudFlare Distributed Web Gateway](https://cloudflare.com/distributed-web-gateway/) - 通过 Cloudflare 提供对以太坊网络的访问，而不是运行您自己的节点
- [Chainstack](https://chainstack.com/) - 共享和专用的以太坊节点即服务（Mainnet、Ropsten、Rinkeby）
- [Alchemy](https://alchemyapi.io/) - 区块链开发平台、以太坊API、节点服务（Mainnet、Ropsten、Rinkeby、Goerli、Kovan）
- [ZMOK](https://zmok.io/) - JSON-RPC 以太网 API (Mainnet, Rinkeby, Front-running Mainnet)
- [Watchdata](https://watchdata.io) - 提供对以太坊区块链的简单可靠的 API 访问

#### 以太测试水龙头（faucet）

- [Rinkeby faucet](https://faucet.rinkeby.io/)
- [Kovan faucet](https://github.com/kovan-testnet/faucet)
- [Ropsten faucet (MetaMask)](https://faucet.metamask.io/)
- [Goerli faucet](https://goerli-faucet.slock.it/)
- [Universal faucet](https://faucets.blockxlabs.com/)
- [Nethereum.Faucet](https://github.com/Nethereum/Nethereum.Faucet) - 一个 C#/.NET 语言实现的水龙头


# 前端 

#### UI 组件

- 在[官方网站](https://reactjs.org/tutorial/tutorial.html)上学习 React 或完成一些[课程](https://egghead.io/courses/the-beginner-s-guide-to-react)
- [React 学习路线](https://github.com/adam-golab/react-developer-roadmap)
- [aragonUI](https://ui.aragon.org) - 包含 Dapp 组件的 React 库
- [components.bounties.network](https://components.bounties.network) - 包含 Dapp 组件的 React 库
- [ui.decentraland.org](https://github.com/decentraland/ui) - 包含 Dapp 组件的 React 库
- [dapparatus](https://github.com/austintgriffith/dapparatus) - 可重用的 React Dapp 组件
- [Metamask ui](https://github.com/MetaMask/metamask-storybook) - Metamask React 组件
- [DappHybrid](https://github.com/Nethereum/Nethereum.DappHybrid) - 一种基于 Web、去中心化的应用程序的跨平台混合托管机制
- [Nethereum.UI.Desktop](https://github.com/Nethereum/Nethereum.UI.Desktop) - 跨平台桌面钱包示例
- [eth-button](https://eth-button.github.io/eth-button/) - 极简捐赠按钮
- [Rimble Design System](https://rimble.consensys.design/) - 去中心化应用程序的适应性组件和设计标准。
- [3Box Plugins](https://docs.3box.io/build/plugins) - 加入用于社交功能的 React 组件。包括评论、个人资料和消息。
- [brave-ui](https://github.com/brave/brave-ui) - 可重用的 React 组件列表，以增强你的 UI
- [DApp frontend security](https://blog.embarklabs.io/news/2020/01/30/dapp-frontend-security/index.html) - 在此文中，作者研究了 DApp 的安全性。

# 项目管理

- [Dework](https://dework.xyz/) | Web3 Trello 具有代币支付、凭证、赏金......
- [Wonderverse](https://www.wonderverse.xyz/) | Jira 的替代品具有直观的任务管理系统，允许 DAO 支付贡献者和在他们的项目中进行协作。

# 更多阅读

#### 受启发于：

- [ETH Dapp 开发者路线图](https://github.com/thecryptoshed/eth-dapp-developer-roadmap)
- [DeFi 防御 DAO 工具](https://github.com/defi-defense-dao/defi-risk-tools-list#developer-tools) 
- [区块链学习路径](https://github.com/protofire/blockchain-learning-path) 
- [一个很棒的去中心化金融项目](https://github.com/ong/awesome-decentralized-finance) 
- [DeFi 工具箱](https://github.com/gweicz/defi-toolkit)
- [区块链工具](https://github.com/nujabes403/blockchains-tools)
- [SAW 列表](https://simpleaswater.com/defi/#analytics)
- [Public APIs](https://github.com/public-apis/public-apis#cryptocurrency)
- [BTC 列表](https://github.com/igorbarinov/awesome-bitcoin)
- [ConsenSys](https://github.com/ConsenSys/ethereum-developer-tools-list)
- [EVM 工具](https://github.com/CoinCulture/evm-tools)
- [Solidity Pro](https://github.com/bkrem/awesome-solidity)
- [知乎](https://zhuanlan.zhihu.com/p/265374061)
- [OpenZeppelin - Contracts / Test Helpers + More ](https://github.com/OpenZeppelin)
- [很棒的以太坊资源列表](https://medium.com/quiknode/awesome-ethereum-resource-lists-dd28a9c17fc1)
- [全面的以太坊开发者资源列表](https://github.com/ConsenSys/ethereum-developer-tools-list/blob/master/README.md)
- [学习智能合约](https://github.com/arbazkiraak/SmartContractLearning)
- [加密经济学](https://github.com/jpantunes/awesome-cryptoeconomics)
- [Tudelft Repo](https://repository.tudelft.nl)
- [阅读列表](https://www.decentralised.co/the-reading-list)还有[这个库](https://github.com/sambacha/compendium)
- [Eth 重入攻击模式](https://github.com/uni-due-syssec/eth-reentrancy-attack-patterns)
- [用于测试智能合约的插件](https://github.com/meherett/pytest-eth)
- [Solidity 函数分析器](https://github.com/EricR/sol-function-profiler)
- [智能合约攻击向量](https://github.com/KadenZipfel/smart-contract-attack-vectors)
- [DeFi 安全列表](https://github.com/freight-chain/defi-sec)
- [DeFi 威胁库](https://github.com/freight-trust/defi-threat)
- [黑客](https://github.com/geekshiv/Smart-Contract-Hacking)
- [Secureum 训练营](https://hackmd.io/@secureum/bootcamp-epoch0-announcement)
- [SCSVS](https://github.com/securing/SCSVS)
- [检查智能合约](https://github.com/tintinweb/smart-contract-inspector)
- [区块链安全夺旗](https://github.com/openblocksec/blocksec-ctfs)
- [Builder 列表](https://based.builders)
- [从 0 到 Web3.0](https://github.com/kay-is/web3-from-zero)


#### 安全与保障：

**|** 阅读 3 个很棒的短文: 

- [所有已知的智能合约端和用户端攻击](https://graph.org/All-known-smart-contract-side-and-user-side-attacks-and-vulnerabilities-in-Web30--DeFi-03-31), 
- [现有的所有 ETH 安全工具](https://graph.org/ETHSec-Tools-02-13), 
- [Solidity 速查表包](https://graph.org/Solidity-Cheatsheets-Pack-03-20) 和 [关于 NFT 安全性的一切](https://graph.org/NFT-security-01-28)
  #
- [区块链安全路线图](https://devansh.xyz/blockchain-security/2021/09/17/genesis-0x01.html) - 本文将铺设一条路径/路线图，用户将沿着这条路径/路线图轻松进入区块链安全领域。
- [荷鲁斯之眼：发现和分析对以太坊智能合约的攻击](https://arxiv.org/pdf/2101.06204.pdf) -调查显示，过去几年攻击次数不一定减少，但某些漏洞的数量保持不变。
- [比特币易受大额交易贿赂攻击的分析](https://arxiv.org/pdf/2105.07501.pdf) -  在这篇论文中，作者设计了一种新颖的贿赂攻击，并表明这种保证可以被极大地破坏。
- [区块链技术对量子攻击的脆弱性](https://arxiv.org/pdf/2105.01815.pdf) - 在这里，作者分析了当今部署的主要基于区块链的加密货币——包括比特币、以太币、莱特币和 ZCash，并确定了量子攻击的风险敞口。
- [BLOCKEYE](https://arxiv.org/pdf/2103.02873.pdf) - 寻找区块链上的 DeFi 攻击。 在这篇论文中，作者提出了 BLOCKEYE，一种针对以太坊区块链上 DeFi 项目的实时攻击检测系统。
- [动态多层区块链网络中的拓扑异常检测](https://arxiv.org/pdf/2106.01806.pdf) - 作者介绍了动态多层网络中结构异常检测的新拓扑视角。
- [用Dafny验证增量默克尔树算法](https://arxiv.org/pdf/2105.06009.pdf) - 作者展示了我们新的和原始的算法正确性证明以及 Dafny 机器可检查的版本。
- [GoHammer 区块链性能测试工具](https://arxiv.org/pdf/2105.00847.pdf) - 该工具将有助于开发更高效的去中心化系统，并将影响降低开发去中心化应用程序项目的成本。
- [EtherClue：对以太坊智能合约攻击的数字调查](https://arxiv.org/pdf/2104.05293.pdf) - 在这项工作中，作者使用专为区块链使用而设计的妥协指标研究了以太坊攻击的事后调查问题。
- [每个可能用例的区块链平台需求分析和评估](https://arxiv.org/pdf/2103.03209.pdf) - 本文档提供了理解区块链及其应用程序的通用模型。
- [关于常数函数做市商隐私的说明](https://arxiv.org/pdf/2103.01193.pdf) -  在本说明中，作者表明，在最合理的对手模型下，CFMM 的常规实现不可能实现隐私，并提供了一些缓解策略。
- [以太坊智能合约中的安全漏洞调查](https://arxiv.org/pdf/2105.06974.pdf) -  本文通过分析这些漏洞的利用案例场景，阐述了8个特定于BT应用层的漏洞。
- [一种检测以太坊智能合约中拒绝服务漏洞的方法](https://arxiv.org/pdf/2106.01340.pdf) -  在本文中，作者提出了一个框架，该框架结合了静态和动态分析来检测由于 ETH 智能合约中的意外恢复而导致的 DoS。
- [AGSolT：Solidity 智能合约自动测试用例生成工具](https://arxiv.org/pdf/2102.08864.pdf) - 作者发现 AGSolT 能够通过这两种方法实现高分支超载，甚至在 Github 上一些最流行的 Solidity 智能合约中发现了一些错误。
- [用于以太坊交易跟踪的时间量快照多图](https://arxiv.org/pdf/2102.08013.pdf) - 作者提出 TASMG 将以太坊交易记录建模为时间数量网络，然后提出 TAW 以通过交易记录有效地嵌入账户，它集成了所提议网络的时间和数量信息。
- [解密加密货币挖矿攻击：一种基于数字取证和动态网络特征的半监督学习方法](https://arxiv.org/pdf/2102.10634.pdf) - 本文解决了使用动态网络特征在通用网络环境中检测加密挖掘攻击的问题。
- [FASTEN：使用智能合约进行公平和安全的分布式投票](https://arxiv.org/pdf/2102.10594.pdf) - 作者证明，隐私泄露的可能性很小，可以忽略不计。 此外，在以太坊上执行 FASTEN 的成本分析与大多数现有选举成本相当。
- [挖矿成本、挖矿奖励和区块链安全之间的相互依赖关系](https://arxiv.org/pdf/2102.08107.pdf) - 本文研究了工作量证明区块链的运营成本在多大程度上与防止攻击的成本有内在联系，以及底层数字账本安全预算在多大程度上与加密货币市场结果相关
- [HyperSec：用于区块链安全监控的可视化分析](https://arxiv.org/pdf/2103.14414.pdf) - HyperSec，一种可视化分析监控工具，可提供一目了然的相关信息，以检测对 Hyperledger Fabric 的持续攻击。
- [以太坊智能合约中的重入漏洞识别](https://arxiv.org/pdf/2105.02881.pdf) - 在本文中，作者提出了一个结合静态和动态分析的框架来检测以太坊智能合约中的重入漏洞。
- [区块链协议安全分析的通用框架](https://arxiv.org/pdf/2009.09480v2.pdf) - 本文提出了一个简约的抽象概念，足以捕获和比较许多著名的无许可区块链协议的属性。
- [Coinbugs：枚举常见的区块链实现级漏洞](https://arxiv.org/pdf/2104.06540.pdf) -  本文面向旨在开始区块链安全审查的安全测试人员和区块链开发人员，作为常见陷阱的参考。
- [智能合约的漏洞和未决问题：系统映射](https://arxiv.org/pdf/2104.12295.pdf) - 本文进行了系统的文献映射，确定了分析 SC 的举措和工具以及如何处理已识别的漏洞。
- [SuMo：Solidity 智能合约的突变测试策略](https://arxiv.org/pdf/2105.03626.pdf) - 作者报告了 SuMo 对开源项目的首次评估，这些项目有可用的测试套件。 作者得到的结果令人鼓舞，他们认为 SuMo 可以有效地帮助开发者交付更可靠的智能合约。
- [区块链的稳定性：去杠杆螺旋和稳定币攻击](https://arxiv.org/pdf/1906.02152.pdf) - 2019 年本文首次发布时首次预测了螺旋式去杠杆化的可能性，随后在 2020 年 Dai 的黑色星期四危机中观察到。
- [区块链系统的匿名信任标记方案](https://arxiv.org/pdf/2010.00206.pdf) - 在本文中，作者提出了一种普遍适用于任何加密货币的区块链系统匿名信任标记方案。
- [以太坊智能合约漏洞的框架和数据集](https://arxiv.org/pdf/2009.02066.pdf) -  在本文中，为了填补空白，作者首先从多个来源收集尽可能多的智能合约错误，并通过扩展 IEEE 软件异常标准分类将这些错误分为 9 类。
- [针对区块链网络中不同矿工行为攻击的安全多链共识方案。](https://arxiv.org/pdf/2106.02383.pdf) - 实验结果表明，PoDT 对 DMB 攻击是安全的，并且在多链环境中比传统的共识方案更有效。
- [联盟链共识机制综述](https://arxiv.org/pdf/2102.12058.pdf) - 本文重点介绍了企业区块链共识算法中的几种最先进的解决方案。
- [提取在 Coq 中测试和验证的智能合约](https://arxiv.org/pdf/2012.09138.pdf) - 作者基于 MetaCoq 的认证擦除将 Coq 程序提取为函数式语言。
- [无需信任、保护隐私的区块链桥](https://arxiv.org/pdf/2102.04660.pdf) - 在本文中，作者提出了一种协议，用于促进无需信任的跨链加密货币传输，以保护桥接取款的隐私。
- [以太坊智能合约开发的安全清单：模式和最佳实践](https://arxiv.org/pdf/2008.04761.pdf) - 作者涵盖了软件生命周期的设计、编码、测试和部署阶段。
- [使用机器学习对智能合约进行动态漏洞检测](https://arxiv.org/pdf/2102.07420.pdf) - 在这项工作中，作者提出了 Dynamit，这是一种用于检测以太坊智能合约中的重入漏洞的监控框架。
- [针对最薄弱的环节：以太坊智能合约中的社会工程攻击](https://arxiv.org/pdf/2105.00132.pdf) - 在这项工作中，作者探讨了智能合约蜜罐之外的新社会工程攻击的可能性和存在性。
- [OptSmart：智能合约的空间高效乐观并发执行](https://arxiv.org/pdf/2102.04875.pdf) - 在本文中，作者开发了一个并发矿工，它通过使用乐观软件并发执行 AU 来提议区块 事务性内存系统 (STM)。
- [DEFECTCHECKER：通过分析 EVM 字节码自动检测智能合约缺陷](https://arxiv.org/pdf/2009.02663.pdf) - 实验结果表明，DefectChecker 在速度和准确性方面都比这些工具表现更好。
- [SmartBugs：一个分析 Solidity 智能合约的框架](https://arxiv.org/pdf/2007.04771.pdf) - 作者展示了它如何通过向工具 SmartCheck 提供一个新的扩展来简化分析工具的集成和比较，改进 基本上检测与 DASP10 类别不良随机性、时间操纵和访问控制相关的漏洞（已识别的漏洞从 11% 增加到 24%）。
- [分析 Solidity 智能合约中的 Gas 泄漏](https://arxiv.org/pdf/2008.05449.pdf) - 在本文中，作者确定了一组影响智能合约部署和交易成本的 19 种 Solidity 代码气味，以及 通过一项涉及 34 名参与者的调查评估此类气味的相关性。
- [在可变挖矿能力下保护平行链协议](https://arxiv.org/pdf/2105.02927.pdf) - 在本文中，作者考虑设计可证明安全的平行链协议，以适应这种挖矿能力的变化 .
- [使用深度神经网络和迁移学习的以太坊智能合约漏洞检测](https://arxiv.org/pdf/2103.12607.pdf) - ESCORT 框架支持对新漏洞类型进行迁移学习，只需对 DNN 模型架构进行最少的修改和重新训练 高架。
- [SCSGuard：以太坊智能合约的深度诈骗检测](https://arxiv.org/pdf/2105.10426.pdf) - 实验结果表明，SCSGuard 实现了高精度 (0.94)、精确度 (0.96\%) 和召回率 (0.98) 针对庞氏骗局和蜜罐骗局，以及新的网络钓鱼智能合约。
- [通过基于区块链的数字孪生和威胁情报保护网络物理系统](https://arxiv.org/pdf/2105.08886.pdf) - 本文重点介绍通过集成人工智能 (AI) 和区块链来保护 CPS，以实现智能和 可信的 DT。
- [区块链互操作性调查：过去、现在和未来趋势](https://arxiv.org/abs/2005.14282) - 在这篇文章中，作者研究了区块链互操作性技术和解决方案，全面概述了区块链互操作性，铺平了道路 该领域系统研究的途径。
- [SoK：透明的不诚实：对区块链的抢先攻击](https://arxiv.org/abs/2106.00667) - 一篇关于安全智能合约设计决策和 DApp 抢先交易可能性的论文。
- [SoK：Oracles from the Ground Truth to Market Manipulation](https://arxiv.org/abs/2106.00667) - 一篇系统化预言机设计方案、展示攻击并讨论攻击缓解策略的论文。

##### Web2 网络安全

- [TryHackMe：通过浏览器完成充满挑战和谜题的房间](https://tryhackme.com/welcome) - 通过实际任务进行网络安全培训

- [揭露：网络安全研究最佳实践的跨行业和供应商不可知标准](https://disclose.io/) - 开源维护者和行业专家通过模板、工具提供协助、信息和帮助的中央来源 , 数据集...

- [Hack The Box](https://www.hackthebox.com/) - 一个黑客的游乐场，可以在促进实践培训体验的协作生态系统中动态地与其他用户竞争

- [OverTheWire](https://overthewire.org/wargames/) - 社区提供的一组兵棋和挑战，用于在有趣的兵棋中学习和实践安全概念。

- [Pentesterlab](https://pentesterlab.com/) - 动手实验，涵盖从基础到高级的不同课程。

- [Portswigger 实验室](https://portswigger.net/web-security/all-labs) - 一组带有附加社区解决方案的 Web 应用程序安全实验室

- [Vulnhub](https://www.vulnhub.com/) - 用户上传经常试图通过利用已知漏洞获得 root 访问权限的“挑战箱”。

##### Web3 网络安全

- [OpenZeppelin 的 Ethernaut](https://ethernaut.openzeppelin.com/) - 在以太坊虚拟机 (EVM) 的上下文中受 [OverTheWire](https://overthewire.org/) 启发的 Web3 战争游戏集合。 每个级别都是一个需要被黑客攻击的智能合约。

- [Damn Vulnerable Defi](https://www.damnvulnerabledefi.xyz/) - 在 DeFi 和智能合约的背景下学习红队网络安全的进攻性安全游乐场。 示例包括用户需要停止系统工作的任务，从合同中取出资金......

- [Damn Vulnerable DeFi | Foundry](https://github.com/nicolasgarcia214/damn-vulnerable-defi-foundry) - 与 Damn Vulnerable DeFi 相同，但在 foundry 开发框架上有些差别.

##### Web3 CTF（夺旗）

- [Capture the Ether](https://capturetheether.com/) - 由一系列分类挑战组成的传统游戏，用户在每次成功挑战后获得积分。 目标是使 isComplete() 函数返回 true。

- [Paradigm CTF](https://ctf.paradigm.xyz/)

#### DeFI

- [Finematics](https://www.youtube.com/c/Finematics/featured) - DeFi 教育视频

- [可组合 DeFi 协议的形式分析](https://arxiv.org/pdf/2103.00540.pdf) - 在本文中，作者提出了一种形式化过程代数技术，以组合方式对 DeFi 协议进行建模，以实现高效的属性验证 .

- [交易费用机制设计](https://arxiv.org/pdf/2106.01340.pdf) - 作者解释了区块链中的费用行为。

- [DeFi: 挑战与过程](https://arxiv.org/pdf/2101.05589.pdf) - 对去中心化金融开端的良好回顾。

- [DeFi 中自动做市商的理论](https://arxiv.org/pdf/2102.11350.pdf) - 作者利用我们的理论正式证明了 AMM 的一组基本属性，表征了结构和经济方面。

- [从银行到 DeFi：借贷市场的演变](https://arxiv.org/pdf/2104.00970.pdf) - 作者讨论了 DeFi 借贷对传统金融体系的持续依赖，并总结了借贷市场的前景 车联网时代的借贷市场。

- [关于 DeFi 协议中盈利交易的即时发现](https://arxiv.org/pdf/2103.02228.pdf) - 在本文中，作者研究了两种允许他们自动创建有利可图的 DeFi 的方法 交易。

- [最大化自动做市商的可提取价值](https://arxiv.org/pdf/2106.01870.pdf) - 在本文中，作者正式将理性矿工描述为在挖矿游戏中遵循最佳策略的玩家。

- [去中心化金融危机](https://arxiv.org/pdf/2002.08099.pdf) - 在本文中，作者探讨了 DeFi 协议的设计缺陷和价格波动如何导致 DeFi 危机。

- [清算： DeFi 前途难料](https://arxiv.org/pdf/2009.13235v4.pdf)- 为了保护协议免受损失，可以清算抵押不足的头寸。 在本文中，作者对可贷资金 (PLF) 协议的清算进行了实证分析。

- [衡量资产可组合性作为 DeFi 集成的代理](https://arxiv.org/pdf/2102.04227.pdf) - 作者试图通过检查“组合”中的交易来了解这种做法对以太坊金融集成的贡献程度 ' 资产 DAI、USDC、USDT、ETH 和代币化 BTC 的衍生品，用于 2020 年计算的全套 3.448 亿以太坊交易。

- [去中心化自治加密货币交易所的动态曲线](https://arxiv.org/pdf/2101.02778.pdf) - 作者在这项工作中提出了一种通过提出动态曲线的想法来构建 AMM 的新方法。

- [去中心化链上交易所的高频交易](https://arxiv.org/pdf/2009.14021.pdf) - 在这项工作中，作者形式化、分析性地阐述并凭经验评估抢先交易的增强变体：三明治攻击， 其中涉及前端和后端运行的受害者 TX。

- [Flashot](https://arxiv.org/pdf/2102.00626.pdf) - DeFi 生态系统闪电贷攻击快照。

- [DeFiRanger](https://arxiv.org/pdf/2104.15068.pdf) - 检测对 DeFi 应用程序的价格操纵攻击。

- [用闪电贷攻击 DeFi 生态系统以获得乐趣和利润](https://arxiv.org/pdf/2003.03810.pdf) - 闪电贷，去中心化金融。 

- [SoK：去中心化金融 (DeFi)](https://arxiv.org/pdf/2101.08778.pdf) - 在此知识系统化 (SoK) 中，作者沿着其主轴描述了 DeFi 生态系统。 SCSGuard：以太坊智能合约的深度诈骗检测

- [来自四种治理令牌分布的经验证据](https://arxiv.org/pdf/2102.10096.pdf) - 本文提供了一个框架来量化区块链应用程序中治理权力的分散。

- [采用基于区块链的去中心化交易所](https://arxiv.org/pdf/2103.08842.pdf) - 作者表明，由于基于区块链的订单执行机制，如果汇率波动，流动性提供者会失去代币价值 交换。

- [Uniswap 市场分析](https://arxiv.org/pdf/1911.03380.pdf) - 关于 Uniswap DEX 活动的最佳研究之一，作者于 2019 年开始研究，最近发布了最新的 2021 年分析。

- [金融 4.0：价值敏感的密码经济系统的设计原则以解决可持续性问题](https://arxiv.org/pdf/2105.11955.pdf) - 作者提供了有关设计密码系统的新见解。

- [去中心化交易所中流动性提供者的行为](https://arxiv.org/pdf/2105.13822.pdf) - 作者旨在了解流动性提供者如何对市场信息做出反应，以及他们如何从提供 DEX 流动性中获益。

- [去中心化交易市场的循环套利](https://arxiv.org/pdf/2105.02784.pdf) - 值得一读。本文表明，借助智能合约技术和以太坊的复制状态机设置，套利策略在 DEX 中比在 CEX 中更容易实施。

- [SoK：从基本事实到市场操纵的预言机](https://arxiv.org/pdf/2106.00667.pdf) - 在此 SoK 中，作者系统化了 oracles 的设计备选方案，展示了攻击并讨论了攻击缓解策略。

- [自动做市商的组成网络](https://arxiv.org/pdf/2106.00083.pdf) - 本文提出了 AMM 组合的数学模型。

- [区块链预言机设计模式](https://arxiv.org/abs/2106.09349) - 在本文中，作者将研究和分析区块链预言机如何向区块链和智能合约提供反馈。

- [CeFi vs. DeFi - 比较中心化金融和去中心化金融](https://arxiv.org/abs/2106.08157) - 在这项工作中，作者系统地分析了 CeFi 和 DeFi 之间的差异，涵盖法律、经济、安全、隐私和市场 操纵。 作者还提供了一种结构化方法来区分 CeFi 和 DeFi 服务。


#### 以太坊域名服务

- [以太坊域名服务：好的、坏的和丑的](https://arxiv.org/pdf/2104.05185.pdf) - 然而，没有现有的工作研究这个新兴系统、ENS 中的安全问题和不当行为。作者通过分析数百万与 ENS 相关的事件日志，展示了 ENS 的第一项研究。


#### 非同质化代币 (NFT):

- [映射 NFT 革命](https://arxiv.org/pdf/2106.00647.pdf) - 市场趋势、贸易网络和视觉特征。

- [ERC 代币市场的公平性](https://arxiv.org/pdf/2102.03721.pdf) - CryptoKitties 的案例研究。

- [NFT：概述、评估、机遇与挑战](https://arxiv.org/pdf/2105.07447.pdf) - 在这份技术报告中，作者从几个方面探讨了 NFT 生态系统。

- [Cryptoart](http://cryptoart.io/) - 顶级艺术家和艺术品。

- [CryptoArtPulse](https://cryptoartpulse.com/) - 实时景象。

- [PumpMyGas](https://pumpmygas.xyz/) - 所有主要 NFT 市场的汽油费实时估算。

- [NonFungible Tracker](https://nonfungible.com/) - NFT 追踪器。

- [NFTS TOP]( https://cryptoslam.io) - NFT 排行。

- 以太坊不可替代代币网络：基于图的 ERC-721 生态系统分析


#### 稳定币:


- [稳定币 2.0](https://arxiv.org/pdf/2006.12388.pdf) - 作者力图为稳定币理论提供坚实的基础，并对稳定币的经济结构进行基于风险的功能表征。

- [降低加密货币的波动性——稳定币调查](https://arxiv.org/pdf/2103.01340.pdf) - 作者通过调查不同类型的稳定币及其稳定性机制，讨论了稳定币如何帮助降低加密货币的波动性。

- [了解算法稳定币的波动性：建模、验证和实证分析](https://arxiv.org/pdf/2101.08423.pdf) - 作者对 Basis Cash 稳定币的真实交易活动进行了系统的实证分析，将理论可能性与 市场观察。

- [T-Cash：可转让的法定支持硬币](https://arxiv.org/pdf/2105.04485.pdf) - 在本文中，作者提出了一种使用区块链技术的可转让电子现金方案，允许用户在系统内不断重复使用硬币。


#### 其它资料：


- [以太坊网络的大数据分析：从区块链到谷歌趋势](https://arxiv.org/pdf/2104.01764.pdf) - 对加密货币价格和搜索趋势的分析表明大玩家的存在（不是普通用户），在价格下跌后操纵市场。

- [用于原子和可扩展交易的基于 DLT 的智能合约架构](https://arxiv.org/pdf/2105.02937.pdf) - 在本文中，作者提出了一种原子的、可扩展的和隐私保护的协议，可以实现安全和动态 更新。 然后开发一个基于智能合约的信用票据系统（CNS），允许参与者在状态通道初始化之前锁定资金，从而提高灵活性和效率。

- [探索以太坊数据存储：成本和性能比较](https://arxiv.org/pdf/2105.10520.pdf) - 在这项工作中，作者检查了一套全面的 ETH 应用程序数据管理方法，并评估了相关成本 气体以及检索性能。

- [关于区块链治理的系统文献综述](https://arxiv.org/pdf/2105.05460.pdf) - 本研究通过 5W1H 问题全面调查区块链治理。

- [区块链分析的通用框架](https://arxiv.org/pdf/1707.01021.pdf) - 作者提出了一个通用框架，支持比特币以太坊上的数据分析——它允许将块数据与来自其他来源的数据集成 , 并将它们组织在数据库中。

- [AMR：具有隐私保护奖励分配的自治硬币混合器](https://arxiv.org/pdf/2010.01056.pdf) - 在这项工作中，作者提出了第一个审查弹性混合器，它可以在保护隐私的情况下奖励其用户 参与系统的方式。

- [区块链数据隐私解决方案技术回顾](https://arxiv.org/pdf/2105.01316.pdf)- 本报告旨在回顾现有的企业区块链技术：EOSIO 驱动系统、Hyperledger Fabric 和 Besu、Consensus Quorum、R3 Corda 和 安永会计师事务所的夜幕降临。

- [区块链系统、技术和应用：方法论视角](https://arxiv.org/pdf/2105.03572.pdf) - 本文首先介绍了区块链的工作原理、研究活动和挑战，并说明了涉及经典的路线图 具有典型区块链用例和主题的方法。 其次，在区块链系统中，详细讨论了如何采用随机过程、博弈论、优化、机器学习和密码学来研究区块链运行过程和设计区块链协议/算法。

- [Ethna：分析以太坊区块链的底层点对点网络](https://arxiv.org/pdf/2010.01373.pdf) - Ethna 实现了一种准确测量以太坊节点度数的新方法。

- [区块链社交网络中的社区检测](https://arxiv.org/pdf/2101.06406.pdf) - 一种新的社区检测算法，专为图上的低秩信号设计，可以帮助基于用户令牌找到用户的社区 订阅。

- [无线区块链网络中的块访问控制：设计、建模和分析](https://arxiv.org/pdf/2104.13144.pdf) - 结果表明 BAC 方法可以帮助网络实现高交易吞吐量，同时提高块 利用和节省计算能力。 同时，展示了交易吞吐量和区块利用率之间的权衡，可以为区块链的实际部署提供指导。

- [对外呼吁区块链和分布式账本技术](https://arxiv.org/pdf/2105.10399.pdf) - 在本文中，作者通过展示一种使区块链和分布式账本技术能够执行的方法表明，这种信念是先入为主的 从区块链/分布式账本技术本身发起的对外部系统的调用。

- [管理区块链系统和应用程序：区块链配置的过程模型](https://arxiv.org/pdf/2105.02118.pdf) - 作者展示了所提出的区块链配置过程模型在四个区块链项目上的适用性

- [关于恒定函数做市商的最佳费用的说明](https://arxiv.org/pdf/2105.13510.pdf) - 作者提出了一个框架，该框架可用于使用过去的交易数据计算现实世界矿池的最佳费用。

- [使用进化博弈论的区块链奖励机制](https://arxiv.org/pdf/2104.05849.pdf) - 在这篇论文中，作者开发了一个可以应用于许多 PoS 区块链的奖励机制框架。

- [智能转换总结](https://arxiv.org/pdf/2105.07663.pdf) - 在这篇论文中，作者提出了一种一阶逻辑的概括，它可以表达无限的余额和。

- [软件初创公司的 100 多个指标 - 多声文献回顾](https://arxiv.org/pdf/1901.04819.pdf) - 使用度量形式的数据可以帮助软件初创公司在不确定性和不确定性中做出正确的决策 有限的资源。

- [区块链网络：比特币、Monero、Zcash、Ethereum、Ripple 和 IOTA 的数据结构](https://arxiv.org/pdf/2103.08712.pdf) - 作者讨论了如何将区块链数据抽象为各种类型的网络，以及 网络抽象如何用于深入了解结构。

- [去中心化金融：基于区块链和智能合约的金融市场](https://research.stlouisfed.org/publications/review/2021/02/05/decentralized-finance-on-blockchain-and-smart-contract- based-financial-markets) - 由 Fabian Schar 撰写，概述了基于区块链的市场以及技术细节，但采用易于理解的格式； 适合该领域新手的好论文。

#### 作者的特别汇总:

- [关于 NFT 安全性的一切](https://graph.org/NFT-security-01-28) 
- [现有的所有 ETH 安全工具](https://graph.org/ETHSec-Tools-02-13)
- [所有优秀的 TG 开发社区](https://graph.org/Crypto-Telegram-Channels--Chats-04-19)
- [所有已知的智能合约端和用户端攻击](https://graph.org/Data-02-14)
- [Solidity A-Z](https://graph.org/Solidity-Cheatsheets-Pack-03-20)
- [所有已知的智能合约端和用户端攻击](https://graph.org/All-known-smart-contract-side-and-user-side-attacks-and-vulnerabilities-in-Web30--DeFi-03-31)
- [所有可能的交易分析、加密货币取证和调查工具在一个注释中列出和参考](https://graph.org/TX-Analysis-tools-04-19)
- [存储加密冷钱包攻击防御方法最佳实践的关键原则](https://graph.org/Key-principles-of-storing-crypto-cold-wallet-attacks-defense-methods-best-practices--Bonus-04-23)


#### 支链

- [POA 网络](https://www.poa.network/)
- [POA 桥](https://bridge.poa.net/)
- [POA 桥用户界面](https://github.com/poanetwork/bridge-ui)
- [POA 桥合约](https://github.com/poanetwork/poa-bridge-contracts)
- [Loom Network](https://github.com/loomnetwork)
- [Matic Network](https://docs.matic.network/)


#### EIP - 1559

- [EIP1559 FAQ](https://notes.ethereum.org/@vbuterin/eip-1559-faq) - EIP 1559 常见问题

- [EIP-1559 以太坊费用市场的动态分析](https://arxiv.org/pdf/2102.10567.pdf)- 作者通过结合博弈论和动力系统的工具，对由此产生的费用市场动态机制进行了全面分析。

- [EIP1559 基础费用的随机特性](https://arxiv.org/pdf/2105.03521.pdf) - 作者解释了为稳定波动的天然气价格而开发的以太坊新定价机制。

- [以太坊区块链的交易费用机制设计：EIP-1559 的经济分析](https://arxiv.org/pdf/2012.00854.pdf) - 本报告评估了该提案的博弈论优势和劣势，并探讨了一些替代设计。


#### 以太坊 2.0

- [Serenity 设计原理](https://notes.ethereum.org/@vbuterin/serenity_design_rationale)
- [规范](https://github.com/ethereum/annotated-spec)
- [Beaconcha](https://beaconcha.in/)
- [Beaconscan](https://beaconscan.com/)
- [以太坊 2.0 统计](https://eth2stats.io/)
- [以太网 2.0 文档](https://docs.ethhub.io/ethereum-roadmap/ethereum-2.0/eth-2.0-phases/)
- [以太网 2.0 客户端](https://docs.ethhub.io/ethereum-roadmap/ethereum-2.0/eth2.0-teams/teams-building-eth2.0/)
- [以太网 2.0 Forks](https://eth2-fork-mon.stokes.io/) 


#### 最大可提取价值/矿工可提取价值


- [量化区块链可提取价值：森林有多黑暗？](https://arxiv.org/pdf/2101.05511v2.pdf) - 作者提供证据表明矿工已经提取了矿工可提取价值 (MEV)，这可能会破坏区块链共识 安全性，如相关工作所示。

- [Flash Boys 2.0：去中心化交易所中的抢先交易、交易重新排序和共识不稳定性](https://arxiv.org/pdf/1904.05234.pdf) - 介绍 MEV 的概念，作品突出了交易带来的巨大、复杂的风险 -排序智能合约中的依赖关系以及传统形式的金融市场剥削适应和渗透区块链经济的方式。

- [Flashbots：Eth2 中的 MEV](https://hackmd.io/@flashbots/mev-in-eth2) - 在这篇文章中，作者研究了 eth2 中的交易排序并分析了支持 MEV 的质押收益率。 然后他们发现 MEV 将显着提高验证者奖励，但可能会加剧 Eth2 参与者之间的不平等。 作者还讨论了 Eth2 中 MEV 的定性方面，例如将在其最大的利益相关者（如交易所和验证者池）之间展开的潜在动态。

- [区块链互操作性调查：过去、现在和未来趋势](https://arxiv.org/abs/2005.14282) - 在这篇文章中，作者研究了区块链互操作性技术和解决方案，全面概述了区块链互操作性，铺平了道路 该领域系统研究的途径。


#### 探讨

- [智能合约研究论坛](https://www.smartcontractresearch.org) 


 #### 黑客事件报告

- [Rekt News](https://rekt.eth.link/leaderboard) - 举报人和 DeFi 侦探向社区展示信息的匿名平台。
- [区块链威胁情报](https://blockthreat.substack.com/) - 涵盖加密货币领域最新安全新闻、工具、事件、漏洞和威胁的时事通讯。支持[此库](https://github.com/openblocksec/blocksec-incidents)
- [Blockchain Graveyard](https://magoo.github.io/Blockchain-Graveyard/) - 涉及区块链的所有大规模安全漏洞或盗窃的列表。


# 工具合集


#### Ethereum Tools

- [现有的所有 ETH 安全工具](https://graph.org/ETHSec-Tools-02-13)
- [Ethstats](https://ethstats.io)
- [ETH Forks](https://forkmon.ethdevops.io) 
- [Node 统计](https://ethernodes.org)
- [EVM 网络列表](https://chainid.network)
- [BIP39 Derivation](https://iancoleman.io/bip39)
- [Vanity Generator](https://github.com/johguse/profanity) 
- [Web Vanity Generator](https://vanity-eth.tk) 
- [Vanity Eth Generators](https://github.com/search?q=eth+vanity)
- [FindETH](https://findeth.io) 
- [Eth Tx Decoder](https://antoncoding.github.io/eth-tx-decoder)
- [Ethereum input data decoder](https://lab.miguelmota.com/ethereum-input-data-decoder)
- [Ethereum Gas Charts](https://ethereumprice.org/gas)
- [Ethereum TxPool Statistics](https://txpool.zengo.com/) 
- [Gas 价格仪表板](https://explore.duneanalytics.com/public/dashboards/qswVMdzbyiiZFdnCDSwx1jfYLOjdaokM4CSGNxsH)
- [The UI from ABI](https://ethcontract.watch)
- [Oracles Club](https://oracles.club)
- [Tx Combo](https://furucombo.app)
- [ETH or ERC-20 Mass-sender](https://disperse.app)
- [BulkSender](https://bulksender.app)
- [ERC20 Meta Token Wrapper](https://github.com/arcadeum/erc20-meta-token) 
- [取消以太坊交易](https://github.com/mds1/Cancel-Ethereum-Transactions)
- [Fees WTF Calculator](https://fees.wtf) 
- [Spend Gas Stats](https://txn.finance) 
- [Pools Stats](https://pools.fyi) 
- [Solhint](https://github.com/protofire/solhint) 
- [Solium](https://github.com/duaraghav8/Solium)
- [Sol-tester](https://github.com/androlo/sol-tester) 
- [Solidity-coverage](https://github.com/sc-forks/solidity-coverage) 
- [TypeChain](https://github.com/ethereum-ts/TypeChain) 
- [Tenderly](https://tenderly.co/)


#### 库

- [dapp-bin](https://github.com/ethereum/dapp-bin) - 以太坊存储库为 Solidity、Serpent 和 LLL 中的许多常见数据结构和实用程序提供实现。
- [Solidity Collections](https://github.com/ethereum/wiki/wiki/Solidity-Collections) - 代码片段和实用程序库的集合。
- [OpenZeppelin](https://openzeppelin.org/) - 构建安全智能合约的框架。

#### 流行的智能合约库

- [Zeppelin](https://github.com/OpenZeppelin/openzeppelin-contracts) - 包含经过测试的可重用智能合约，如 SafeMath 和 OpenZeppelin SDK [库](https://github.com/OpenZeppelin/openzeppelin-sdk) 用于智能合约 可升级性
- [cryptofin-solidity](https://github.com/cryptofinlabs/cryptofin-solidity) - Solidity 库的集合，用于在以太坊上构建安全且高效的智能合约。
- [模块化库](https://github.com/Modular-Network/ethereum-libraries) - 一组为使用以太坊虚拟机在区块链上使用而构建的包
- [日期时间库](https://github.com/bokkypoobah/BokkyPooBahsDateTimeLibrary) - 一个处理 Solidity 日期和时间的库
- [Aragon](https://github.com/aragon/aragon) - DAO 协议，包含 [aragonOS 智能合约框架](https://github.com/aragon/aragonOS)，重点关注可升级性和治理
- [ARC](https://github.com/daostack/arc) - DAO 的操作系统和 DAO 堆栈的基础层。
- [0x](https://github.com/0xProject) - DEX 协议
- [带证明的代币库](https://github.com/sec-bit/tokenlibs-with-proofs) - 包含代币合约的正确性证明，给定规格和高级属性。
- [Provable API](https://github.com/provable-things/ethereum-api) - 提供使用 Provable 服务的合约，允许链下操作、数据获取和计算。
- [ABDK Libraries for Solidity](https://github.com/abdk-consulting/abdk-libraries-solidity) - 定点（64.64 位）和符合 IEEE-754 标准的四精度（128 位）浮点数学库，用于 Solidity

#### 智能合约模式

- [Dappsys：安全、简单、灵活的以太坊合约构建块](https://github.com/dapphub/dappsys)
- [MakerDAO](https://github.com/makerdao/maker-otc)
- [The TAO](https://github.com/ryepdx/the-tao)
- [Dapp 1-10 天](https://steemit.com/@nikolai)
- [Dapp 11-25 天](https://steemit.com/@nexusdev)
- [OpenZeppelin Contracts：Solidity 语言的可重用和安全智能合约的开放框架。](https://github.com/OpenZeppelin/openzeppelin-contracts)
- [关于安全审计最佳实践的博客](https://blog.openzeppelin.com/)
- [Advanced Workshop with Assembly](https://github.com/androlo/solidity-workshop)
- [Simpler Ethereum Multisig](https://medium.com/@ChrisLundkvist/exploring-simpler-ethereum-multisig-contracts-b71020c19037) - especially section _Benefits_
- [CryptoFin Solidity 审计清单](https://github.com/cryptofinlabs/audit-checklist) - 常见发现的清单，以及在审计主网启动合同时要注意的问题。
- [aragonOS：用于构建 DAO、Dapp 和协议的智能合约框架](https://hack.aragon.org/docs/aragonos-intro.html)
- [检查效果交互模式](https://fravoll.github.io/solidity-patterns/checks_effects_interactions.html)

#### 可升级性

- [Blog von Elena Dimitrova, Dev at colony.io](https://blog.colony.io/author/elena/)
- [库驱动开发](https://blog.aragon.org/library-driven-development-in-solidity-2bebcaf88736)
- [高级 Solidity 代码部署技巧](https://blog.aragon.org/advanced-solidity-code-deployment-techniques-dc032665f434/)
- [OpenZeppelin 代理库](https://blog.openzeppelin.com/proxy-libraries-in-solidity-79fbe4b970fd/)


#### 开发者工具

- [CryptoFin Solidity 审计清单](https://github.com/cryptofinlabs/audit-checklist) - 常见发现的清单，以及在审计主网启动合同时要注意的问题。
- [MythX](https://mythx.io/) - 以太坊开发者的安全验证平台和工具生态
- [Mythril](https://github.com/ConsenSys/mythril) - 开源 EVM 字节码安全分析工具
- [Oyente](https://github.com/melonproject/oyente) - 替代静态智能合约安全分析
- [Securify](https://securify.chainsecurity.com/) - 以太坊智能合约的安全扫描器
- [SmartCheck](https://tool.smartdec.net/) - 静态智能合约安全分析器
- [Ethersplay](https://github.com/crytic/ethersplay) - EVM 反汇编器
- [Evmdis](https://github.com/Arachnid/evmdis) - EVM 反汇编器的替代品
- [Hydra](https://github.com/IC3Hydra/Hydra) - 加密经济合约安全框架、去中心化安全赏金
- [Solgraph](https://github.com/raineorshine/solgraph) - 可视化智能合约安全分析的 Solidity 控制流
- [Manticore](https://github.com/trailofbits/manticore) - 智能合约和二进制文件的符号执行工具
- [Slither](https://github.com/crytic/slither) - Solidity 静态分析框架
- [Adelaide](https://github.com/sec-bit/adelaide) - Solidity 编译器的 SECBIT 静态分析扩展
- [solc-verify](https://github.com/SRI-CSL/solidity/) - Solidity 智能合约的模块化验证器
- [Solidity 安全博客](https://github.com/sigp/solidity-security-blog) - 已知攻击向量和常见反模式的综合列表
- [Awesome Buggy ERC20 Tokens](https://github.com/sec-bit/awesome-buggy-erc20-tokens) - 影响代币的 ERC20 智能合约漏洞合集
- [免费智能合约安全审计](https://callisto.network/smart-contract-audit/) - 来自 Callisto Network 的免费智能合约安全审计
- [Piet](https://piet.slock.it) - 一个可视化的 Solidity 架构分析器

#### 前端以太坊 API


- [Web3.js](https://github.com/ethereum/web3.js/) - Javascript Web3
- [Eth.js](https://github.com/ethjs) - Javascript Web3 的替代品
- [Ethers.js](https://github.com/ethers-io/ethers.js/) - Javascript Web3 的替代品, 有实用的实用程序和钱包功能
- [light.js](https://github.com/paritytech/js-libs/tree/master/packages/light.js) 为轻客户端优化的高级响应式 JS 库。
- [Web3Wrapper](https://github.com/0xProject/0x-monorepo/tree/development/packages/web3-wrapper) - Typescript Web3 替代品
- [Ethereumjs](https://github.com/ethereumjs/) - 以太坊实用函数集合，如 [ethereumjs-util](https://github.com/ethereumjs/ethereumjs-util) 和 [ethereumjs-tx](https://github.com/ethereumjs/ethereumjs-tx)
- [Alchemy-web3.js](https://github.com/alchemyplatform/alchemy-web3) - 具有自动重试功能的 Javascript Web3 包装器，可访问 [Alchemy 的增强 API](https://docs.alchemyapi.io/documentation/alchemy-web3/enhanced-web3-api)，以及强大的 websocket 连接。
- [flex-contract](https://github.com/merklejerk/flex-contract) 与 [flex-ether](https://github.com/merklejerk/flex-ether) - 用于与智能合约交互和进行交易的现代、零配置、高级库。
- [ez-ens](https://github.com/merklejerk/ez-ens) - 简单、零配置的以太坊名称服务地址解析器。
- [web3x](https://github.com/xf00f/web3x) - web3.js 的 TypeScript 端口。好处包括微型构建和完整的类型安全，包括与合同交互时。
- [Nethereum](https://github.com/Nethereum/) - 跨平台以太坊开发框架
- [dfuse](https://github.com/dfuse-io/client-js) - 使用 [dfuse Ethereum API](https://dfuse.io) 的 TypeScript 库
- [Drizzle](https://github.com/truffle-box/drizzle-box) - 将前端连接到区块链的 Redux 库
- [Tasit SDK](https://github.com/tasitlabs/tasitsdk) - 用于使用 React Native 制作原生移动以太坊 dapp 的 JavaScript SDK
- [useMetamask](https://github.com/mdtanrikulu/use-metamask) - 自定义 React Hook，用于管理 Ethereum ĐApp 项目中的 Metamask
- [WalletConnect](https://walletconnect.org/) - 用于将钱包连接到 Dapps 的开放协议
- [Subproviders](https://0x.org/docs/tools/subproviders) - 与 [Web3-provider-engine](https://github.com/MetaMask/web3-provider-engine) 结合使用的几个有用的子提供者（包括一个 LedgerSubprovider，用于为你的 dApp 添加 Ledger 硬件钱包支持）
- [ethvtx](https://github.com/ticket721/ethvtx) - 以太坊就绪且与框架无关的 redux 存储配置。 [文档地址](https://ticket721.github.io/ethvtx/)
- Strictly Typed - Javascript 替代品
- [elm-ethereum](https://github.com/cmditch/elm-ethereum)
- [purescript-web3](https://github.com/f-o-a-m/purescript-web3)
- [ChainAbstractionLayer](https://github.com/liquality/chainabstractionlayer) - 使用单一界面与不同的区块链（包括以太坊）进行通信。
- [Delphereum](https://github.com/svanas/delphereum) - 以太坊区块链的 Delphi 接口，允许为 Windows、macOS、iOS 和 Android 开发原生 dApp。
- [Torus](https://tor.us/) - 开源 SDK，用于构建具有无缝入职用户体验的 dapp
- [Fortmatic](https://fortmatic.com/) - 一个简单易用的 SDK，无需扩展或下载即可构建 web3 dApp。
- [Portis](https://portis.io/) - 带有 SDK 的非托管钱包，无需安装任何东西即可轻松与 DApp 交互。
- [create-eth-app](https://github.com/paulrberg/create-eth-app) - 使用一个命令创建 Ethereum 支持的前端应用程序。
- [Scaffold-ETH](https://github.com/austintgriffith/scaffold-eth) - 初学者友好的 forkable github，用于开始构建智能合约。
- [Jolly Roger](https://jolly-roger.eth.link/) - 使用 ethereum、buidler、svelte 和 thegraph 的 dApp 框架
- [Notify.js](https://blocknative.com/notify) - 向你的用户发送实时通知。凭借对加速和取消的内置支持，Blocknative Notify.js 可帮助用户自信地进行交易。Notify.js 易于集成和快速定制。

#### 后端以太坊 API

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
- [Eventeum](https://github.com/ConsenSys/eventeum) - 以太坊智能合约事件和后端微服务之间的桥梁，由 Kauri 用 Java 编写
- [Ethereumex](https://github.com/mana-ethereum/ethereumex) - 用于以太坊区块链的 Elixir JSON-RPC 客户端
- [Ethereum-jsonrpc-gateway](https://github.com/HydroProtocol/ethereum-jsonrpc-gateway) - 允许你运行多个以太坊节点以实现冗余和负载平衡目的的网关。可以作为 Infura 的替代品（或在其之上）运行。用 Go 语言编写。
- [EthContract](https://github.com/AgileAlpha/eth_contract) - 在 Elixir 中帮助查询 ETH 智能合约的一组辅助方法
- [Ethereum Contract Service](https://github.com/mesg-foundation/service-ethereum-contract) - 一种 MESG 服务，可根据其地址和 ABI 与任何以太坊合约进行交互。
- [Ethereum Service](https://github.com/mesg-foundation/service-ethereum) - 一个 MESG 服务，用于与来自以太坊的事件进行交互并与之交互。
- [Marmo](https://marmo.io/) - 用于简化与以太坊交互的 Python、JS 和 Java SDK。 使用中继器将交易成本卸载给中继器。
- [Ethereum 日志框架](https://bitbucket.csiro.au/users/kli039/repos/ethereum-logging-framework/browse) - 为以太坊应用程序和网络提供高级日志记录功能，包括查询语言、查询处理器和日志记录代码生成

#### 以太网客户端

- [Besu](https://besu.hyperledger.org/en/latest/) - 在 Apache 2.0 许可下开发并用 Java 编写的开源以太坊客户端。 该项目由 Hyperledger 托管。
- [Geth](https://geth.ethereum.org/docs/) - Go 客户端
- [Erigon](https://github.com/ledgerwatch/erigon) - 建立在效率边界上的以太坊客户端的主要 Go 实现
- [OpenEthereum](https://github.com/openethereum/openethereum) - Rust 客户端，以前称为 Parity。
- [Aleth](https://github.com/ethereum/aleth) - C++ 客户端
- [Nethermind](https://github.com/NethermindEth/nethermind) - .NET Core 客户端
- [Infura](https://infura.io/) - 提供符合以太坊客户端标准的 API 的托管服务
- [Trinity](https://trinity.ethereum.org/) - 使用 [py-evm](https://github.com/ethereum/py-evm) 的 Python 客户端
- [Ethereumjs](https://github.com/ethereumjs/ethereumjs-client) - 使用 [ethereumjs-vm](https://github.com/ethereumjs/ethereumjs-vm) 的JS 客户端 
- [Seth](https://github.com/dapphub/dapptools/tree/master/src/seth) - Seth 是一个以太坊客户端工具——就像“命令行的 MetaMask”
- [Mustekala](https://github.com/musteka-la/mustekala) - Metamask 的以太坊轻客户端项目
- [Exthereum](https://github.com/exthereum/blockchain) - Elixir 客户端
- [EWF Parity](https://github.com/energywebfoundation/energyweb-ui) - Tobalaba 测试网络的 Energy Web Foundation 客户端
- [Quorum](https://github.com/jpmorganchase/quorum) - [JP Morgan](https://jpmorgan.com/quorum) 支持数据隐私的以太坊许可实施
- [Awesome Quorum](https://github.com/ConsenSys/awesome-quorum) - 在 ConsenSys Quorum 上构建的优秀软件、库、工具等的精选列表。
- [Mana](https://github.com/mana-ethereum/mana) - 用 Elixir 编写的以太坊全节点实现。
- [Chainstack](https://chainstack.com/) - 提供共享和专用 Geth 节点的托管服务
- [QuikNode](https://quiknode.io/) - 具有 API 访问和节点即服务的区块链开发人员云。
- [Watchdata](https://watchdata.io) - 提供对以太坊区块链的简单可靠的 API 访问


#### 存储

- [IPFS](https://ipfs.io/) - 去中心化存储和文件引用
- [Mahuta](https://github.com/ConsenSys/Mahuta) - 具有附加搜索功能的 IPFS 存储服务，以前是 IPFS-Store
- [OrbitDB](https://github.com/orbitdb/orbit-db) - IPFS 之上的去中心化数据库
- [JS IPFS API](https://github.com/ipfs/js-ipfs-http-client) - IPFS HTTP API 的客户端库，用 JavaScript 实现
- [TEMPORAL](https://github.com/RTradeLtd/Temporal) - 容易上手的 API， 用于 IPFS 和其他分布式/去中心化存储协议
- [PINATA](https://pinata.cloud) - 使用 IPFS 的最简单方法
- [Swarm](https://swarm-gateways.net/) - 分布式存储平台和内容分发服务，以太坊 web3 堆栈的原生基础层服务
- [Infura](https://infura.io/) - 托管 IPFS API 网关和固定服务
- [3Box Storage](https://docs.3box.io/api/storage) - 用于用户控制的分布式存储的 api。 建立在 IPFS 和 Orbitdb 之上。
- [Aleph.im](https://aleph.im/) - 与 ETH 和 IPFS 兼容的链下激励点对点云项目（数据库、文件存储、计算和 DID）
- [Fleek](https://fleek.co/) - 类似于 netlify，但使用 ipfs 来托管网站。

#### Bootstrap/开箱即用的工具

- [Truffle boxes](https://trufflesuite.com/boxes) - 以太坊生态系统的封装组件
- [Create Eth App](https://github.com/paulrberg/create-eth-app) - 使用一个命令创建以太坊支持的前端应用程序
- [Besu 私有网络](https://besu.hyperledger.org/en/stable/Tutorials/Quickstarts/Azure-Private-Network-Quickstart/) - 在 Docker 容器中运行 Besu 节点的私有网络
- [Testchains](https://github.com/Nethereum/TestChains) - 用于快速响应 (PoA) 的预配置 .NET 开发链
- [Blazor/Blockchain Explorer](https://github.com/Nethereum/NethereumBlazor) - Wasm 区块链浏览器（功能示例）
- [Local Raiden](https://github.com/ConsenSys/Local-Raiden) - 在 docker 容器中运行本地雷电网络用于演示和测试目的
- [私有网络部署脚本](https://github.com/ConsenSys/private-networks-deployment-scripts) - 私有 PoA 网络的开箱即用部署脚本
- [Parity Demo-PoA 教程](https://wiki.parity.io/Demo-PoA-tutorial.html) - 分步教程构建具有 2 个节点的 PoA 测试链，具有 Parity 权威轮共识
- [本地以太网网络](https://github.com/ConsenSys/local_ethereum_network) - 私有 PoW 网络的开箱即用部署脚本
- [Kaleido](https://kaleido.io/) - 使用 Kaleido 启动联盟区块链网络。 非常适合 PoC 和测试
- [Cheshire](https://github.com/endless-nameless-inc/cheshire) - CryptoKitties API 和智能合约的本地沙箱实现，可作为 Truffle Box 使用
- [aragonCLI](https://github.com/aragon/aragon-cli) - aragonCLI 用于创建和开发 Aragon 应用程序和组织。
- [ColonyJS](https://github.com/JoinColony/colonyJS) - 提供用于与 Colony Network 智能合约交互的 API 的 JavaScript 客户端。
- [ArcJS](https://github.com/daostack/arc.js) - 促进 Javascript 应用程序访问 DAOstack Arc 以太网 智能合约的库。
- [Arkane Connect](https://docs.arkane.network/pages/connect-js.html) - 提供用于与 Arkane Network 交互的 API 的 JavaScript 客户端，Arkane Network 是用于构建用户友好的 dapp 的钱包提供商。
- [Onboard.js](https://blocknative.com/onboard) - Blocknative Onboard 是为您的项目添加多钱包支持的快捷方式。 Onboard 为 20 多个独特的硬件和软件钱包提供内置模块，为您节省时间和麻烦。
- [web3-react](https://github.com/NoahZinsmeister/web3-react) - 用于构建单页以太坊 dApp 的 React 框架

#### 以太坊 ABI（应用程序二进制接口）工具

- [ABI decoder](https://github.com/ConsenSys/abi-decoder) - 用于解码来自以太坊交易的数据参数和事件的库
- [ABI-gen](https://github.com/0xProject/0x-monorepo/tree/development/packages/abi-gen) - 从合同 ABI 生成 Typescript 合同包装器。
- [Ethereum ABI UI](https://github.com/hiddentao/ethereum-abi-ui) - 从以太坊合约 ABI 自动生成 UI 表单字段定义和关联的验证器
- [headlong](https://github.com/esaulpaugh/headlong/) - Java 中类型安全的合约 ABI 和递归长度前缀库
- [EasyDapper](https://www.easydapper.com) - 从 Truffle 工件生成 dapps，在公共/私人网络上部署合约，提供实时可定制的公共页面以与合约交互。
- [One Click dApp](https://oneclickdapp.com) - 使用 ABI 在唯一的 URL 上即时创建 dApp。
- [Truffle Pig](https://npmjs.com/package/trufflepig) - 一个开发工具，提供一个简单的 HTTP API 来查找和读取 Truffle 生成的合约文件，以供在本地开发期间使用。 通过 http 提供新的合同 ABI。
- [Ethereum Contract Service](https://github.com/mesg-foundation/service-ethereum-contract) - 一种 MESG 服务，可根据其地址和 ABI 与任何以太坊合约进行交互。
- [Nethereum-CodeGenerator](https://github.com/StefH/Nethereum-CodeGenerator) - 基于网络的生成器，它基于 Solidity 智能合约创建基于 Nethereum 的 C# 接口和服务。


# 测试工具

- [Truffle Teams](https://trufflesuite.com/teams) - Truffle 项目的零配置持续集成
- [Solidity code coverage](https://github.com/0xProject/0x-monorepo/tree/development/packages/sol-coverage) - Solidity 代码覆盖工具
- [Solidity coverage](https://github.com/sc-forks/solidity-coverage) -  Solidity 智能合约代码覆盖工具的替代品
- [Solidity function profiler](https://github.com/EricR/sol-function-profiler) - Solidity 合约函数分析器
- [Sol-profiler](https://github.com/Aniket-Engg/sol-profiler) - 更新的 Solidity 智能合约分析器的替代品
- [Espresso](https://github.com/hillstreetlabs/espresso) - 快速、并行、热重载的 solidity 测试框架
- [Eth tester](https://github.com/ethereum/eth-tester) - 用于测试以太坊应用程序的工具套件
- [Cliquebait](https://github.com/f-o-a-m/cliquebait) - 使用非常类似于真实区块链网络的 docker 实例简化智能合约应用程序的集成和接受测试
- [Hevm](https://github.com/dapphub/dapptools/tree/master/src/hevm) - hevm 项目是以太坊虚拟机 (EVM) 的实现，专门用于单元测试和调试智能合约
- [Ethereum graph debugger](https://github.com/fergarrui/ethereum-graph-debugger) - Solidity 图形化调试器
- [Tenderly CLI](https://github.com/Tenderly/tenderly-cli) - 使用人类可读的堆栈跟踪加快您的开发
- [Solhint](https://github.com/protofire/solhint) - Solidity linter，为智能合约验证提供安全性、风格指南和最佳实践规则
- [Ethlint](https://github.com/duaraghav8/Ethlint) - Linter 用于识别和修复 Solidity（前身为 Solium）中的样式和安全问题
- [Decode](https://github.com/hacker-DOM/decode) - 解析 tx 提交到本地 testrpc 节点的 npm 包，使它们更具可读性和更容易理解
- [truffle-assertions](https://github.com/rkalis/truffle-assertions) - 一个带有额外断言和实用程序的 npm 包，用于使用 truffle 测试 Solidity 智能合约。 最重要的是，它增加了断言特定事件是否已经（未）发出的能力。
- [Psol](https://github.com/Lamarkaz/psol) - Solidity 词法预处理器，具有 mustache.js 风格的语法、宏、条件编译和自动远程依赖包含。
- [solpp](https://github.com/merklejerk/solpp) - Solidity 预处理器和扁平化器，具有全面的指令和表达式语言、高精度数学和许多有用的辅助函数。
- [Decode and Publish](https://flightwallet.github.io/decode-eth-tx/) – 解码并发布原始以太坊 tx。 类似 https://live.blockcypher.com/btc-testnet/decodetx/
- [Doppelgänger](https://getdoppelganger.io/) - 用于在单元测试期间模拟智能合约依赖项的库。
- [rocketh](https://github.com/wighawag/rocketh) - 一个简单的库来测试以太坊智能合约，允许使用您选择的任何 web3 库和测试运行器。
- [pytest-cobra](https://github.com/cobraframework/pytest-cobra) - PyTest 插件，用于测试以太坊区块链的智能合约。


#### 交易可视化、评分和跟踪：

| 查看作者的方法，仔细阅读[推文](https://twitter.com/officer_cia/status/1493395239905734667?s=20&t=rFmBq_f9juLPNWslwrnB7Q)的所有部分

- [BlockPath](http://blockpath.com) 
- [Maltego](http://maltego.com) 
- [GraphSense](http://graphsense.info) 
- [AML Bot Investigation Regime](https://amlbot.com) 
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
- [Visual List](https://www.lopp.net/bitcoin-information/visualizations.html)
- [GLP](https://glprotocol.com/)
- [BreadCrumbs](https://www.breadcrumbs.app)
- [Tenderly](https://tenderly.co/)
- [Dune](https://dune.xyz/)
- [ETH Detective](https://www.ethtective.com/)


## 支持此项目：

支持对我来说**非常**重要，有了它我可以花更少的时间在工作上做我喜欢做的事——教育 DeFi 和加密货币用户： :sparkling_heart:

如果你想支持我的工作，你可以给我捐款，地址是：

**0xB25C5E8fA1E53eEb9bE3421C59F6A66B786ED77A** — ERC20 & ETH (officercia.eth)

**17Ydx9m7vrhnx4XjZPuGPMqrhw3sDviNTU** - BTC

##


(👍 ͡❛ ͜ʖ ͡❛)👍

