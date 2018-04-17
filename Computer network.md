# Computer Network(From top to bottom)



## Chapter 1

- 所有设备（电脑、游戏机、家用电器）都称为**主机**（host）、**端系统**（end system）。

- **端系统**通过**通信链路**（communication link）和**分组交换机**（packet switch）连接到一起。

- 链路**传输速率**以**bit/s**或者**bps**。

- 当端系统传输数据给另一个端系统，发送端将**报文**（message）**分段**，每段加上**首部字节**。由此形成的信息包称为**分组**（packet）。

- 分组交换机从一条**入通信链路**接收到达的分组，并从它的**出通信链路**转发该分组。

- 分组交换机包括**路由器**（router）和**链路层交换机**（link-layer switch）。

  链路层交换机通常用于**接入网**中

  路由器通常用于**网络核心**中

- 从发送端到接收端，一个**分组**所经历的一系列**通信链路**和**分组交换机**称为通过该网络的**路径**（path）。

- 端系统通过**因特网服务提供商**（Internet Service Provider, ISP）接入因特网。

  每个ISP是一个由多个**分组交换机**和多段**通信链路**组成的网络

- 端系统、分组交换机和其他因特网部件都要运行一系列**协议**（protocol）。

  **TCP**（Transmission Control Protocol, 传输控制协议）

  **IP**（Internet Protocol, 网际协议）定义了在路由器和端系统之间发送和接收的**分组格式**

- 主机可分为**客户**(client)和**服务器**(server)。

- **接入网**（access network）是指将端系统连接到其**边缘路由器**（edge router）的**物理链路**。

  边缘路由器是端系统到任何其他远程端系统上的**第一台路由器**。

  - 家庭接入：数字用户线（DIgital Subscriber Line, DSL）、电缆、FTTH（fible to the home）、拨号、卫星
  - 企业（和家庭）接入：以太网和WiFi
  - 广域无线接入：4G、LTE

- 物理媒体（略）

- 分组以等于该**线路最大传输速率**的速度传输通过通信电路。因此，如果某源端主机或者分组交换机经过一条链路发送一个**L**比特的分组，链路的传输速率为**R**比特/秒，则传输该分组的时间为**L/R**。

- 多数分组交换机在链路的输入端使用**存储转发传输**（store-and-forward transmission）机制。

- N条速率为R的链路组成的路径（N-1个路由器），从源到目的地发送一个分组：

  ![Pic01](https://raw.githubusercontent.com/JIAHONGZHANG/Computer-network/master/src/Pic01.png)

- 每个分组交换机有多条链路与之相连。对于每条相连的链路，该分组交换机具有**输出缓存**（output buffer）（也被称为**输出队列** output queue），它用于**存储路由器准备发往哪条链路的分组**。

- 如果到达的分组需要传输到某条链路，但发现该链路正在忙于传输其他分组，该到达分组必须**在输出缓存中等待**。因此，除了储存转发时延外，分组还要城市输出缓存的**排队时延**（queue delay）。

- 缓存空间有限，一个到达的分组可能发现该缓存已经被其他等待传输的分组完全充满。在此情况下，将出现**分组丢失**（丢包 packet lost）。

- 每台路由器具有一个**转发表**（forwarding table），用于将目的地的地址（或目的地地址的一部分）映射成为输出链路。

- 电路交换（circuit switching）和分组交换（packet switching）是通过网络链路和交换机移动数据的两种基本的方法。考虑餐厅订餐服务属于电路交换，不订餐服务属于分组交换。

  假设两台临近交换机之间的每条链路具有1Mbps传输速率，总共有四台主机，则每个端到端电路交换连接获得250kbps专用的传输速率。 

- 四种类型时延：**结点处理时延**（nodal processing delay）、**排队时延**（queuing delay）、**传输时延**（transmission delay）、**传播时延**（propagation delay），这些时延累加起来就是**结点总时延**（total nodal delay）。

- 检查分组首部和决定将该分组导向何处多需要的时间是**处理时延**的一部分。

- 在队列中，当分组在链路上等待传输时，它受到**排队时延**，同时排队时延是**最容易影响**网络加载。

- 传输时延
  $$
  d_{端到端}=N{L\over{R}}
  $$
  ​

- 从该链路的起点到路由器B传播所需要的时间是**传播时延**。

- 传输时延L/R，传播时延d/s。

- 端到端时延，Pic02是Pic01的一般式

  ![Pic02](https://raw.githubusercontent.com/JIAHONGZHANG/Computer-network/master/src/Pic02.png)

  端到端时延假设排队时延微不足道。

- 计算机网络中的吞吐量（略）

- 各层的所有协议被称为**协议栈**（protocol stack）。因特网的协议栈由5个层次组成：

  |       中文名       |      英文名       |
  | :----------------: | :---------------: |
  |       应用层       | Application layer |
  |       运输层       |  Transport layer  |
  | 网络层（一种协议） |   Network layer   |
  |       链路层       |  Data link layer  |
  |       物理层       |  Physical layer   |

  ​

- 应用层是网络应用程序及它们的应用层协议存留的地方。因特网的应用层包括**HTTP**（提供web文档的请求和传送），**SMTP**（提供电子邮件报文的传输）和**FTP**（提供两个端系统之间的文件传送）。这种位于应用层的信息分组称为**报文**（message）。

- 运输层在应用程序端点之间传送应用层报文。两个运输协议，**TCP**和**UDP**，利用其中任意一个都能运输应用层报文。我们把运输层分组称为**报文段**（segment）。

- 网络层负责将被称为**数据报**（datagram）的网络层分组从**一台主机移动到另一台主机**。

  在一台源主机中的运输层协议（TCP或UDP）向网络层提交运输层**报文段**和**目的地**，就像通过邮政服务提供目的地址。

  网络层包括著名的**IP协议**，该协议定义了数据报中各个字段以及端系统和路由器如何作用于这些字段。

  网络层也包括决定路由的**路由选择协议**。

- 为了将分组从一个结点（主机或者路由器）移动到路径上的下一个结点，网络层必须依靠链路层的服务。

  链路层的协议包括以太网、WiFi和电缆接入网的DOCSIS协议。

  链路层分组称为**帧**（frame）。

- 物理层（略）

- 封装（略）


## Chapter 2

- 在**客户-服务器体系结构**（client-server architecture）中，有一个总是打开的主机称为服务器，它服务于来自许多其他称为客户的主机的要求。在此结构中，**客户间不相互通信**。

- **P2P体系结构**（P2P architecture）中，对位于数据中心的专用服务器有最小的（或者没有）依赖。相反，应用程序在间断连接的主机对之间使用直接通信，这些主机对被称为**对等方**。

- 在两个不同端系统上的**进程**（process），通过跨越计算机网络交换**报文**而相互通信。**发送进程**生成并向网络中发送报文；**接收进程**接收这些报文并可能将报文发送回去进行响应。

- 对每对通信进程，我们通常将这两个进程之一标识为**客户**（client），而另一个进程标识为**服务器**（server）。对于Web而言，浏览器是客户进程，Web服务器是一台服务器进程。对于P2P文件共享，下载文件的对等方称为客户，上载文件的对等方为服务器。

- 在给定的一对进程的通信对话中，发起通信的进程为客户，在会话开始时等待联系的进程是服务器。

- 进程通过一个称为**套接字**（socket）的软件接口向网络发送报文和从网络接收报文。套接字是同一台主机内应用层和运输层之间的接口。

- 由于套接字是建立网络应用程序的可编程接口，因此套接字也被称为**应用程序编程接口**（Application Programming Interface, API）。

- 发送进程除了需要知道报文送往目的地的主机地址（IP）外，发送进程还需要指定运行在接收主机上的接收进程（接收套接字）。目的地**端口号**（port number）用于这个目的。

- 运输层协议负责将该报文进入接收进程的套接字。一个运输层协议能够为其应用程序提供：可靠数据传输、吞吐量、定时和安全性。

  可靠数据传输：保证应用程序的一端发送的数据正确、完全地交付给该应用程序的另一端。

  吞吐量：发送进程能够向接收进程交付比特的速率。如因特网电话应用程序对语音以32kbps的速率进行编码，那么它也必须以这种速率向网络发送数据，并向接收应用程序交付数据。

  定时：（例子）发送方注入进套接字中的每个比特到达接收方的套接字不迟于100ms。应用在因特电话、虚拟环境、电话会议和多方游戏。

  安全性：运输协议能够为应用程序提供一种或多种安全性服务。

- **TCP服务模型**包括**面向连接服务**和**可靠数据传输服务**。还拥有**拥塞控制机制**。

- **UDP服务**是一种**不提供不必要服务的轻量级运输协议**。UDP在两个进程通信前没有握手过程。UPD**不保证**该报文将到达接收进程。到达接收进程的报文也可能是乱序到达的。

- TCP和UDP都没有提供吞吐量和定时的保证。

- Web的应用层协议是超文本传输协议（HyperText Transfer Protocol, HTTP）。HTTP定义了这些报文的结构以及客户和服务器进行报文交换的方式。**HTTP使用了TCP作为它的支撑运输协议**。

  HTTP/1.0包括的方法有：GET、POST和HEAD

  HTTP/1.1包括的方法有：GET、POST、HEAD、PUT、DELETE、TRACE、OPTIONS、CONNECT、PATCH

- 服务器向客户发送被请求的文件，而不存储如何关于该客户的状态信息。所以HTTP是一个**无状态协议**（stateless protocol）。

- RTT的定义：

  > We define the round-trip time, which is the time it takes for a small packet to travel from client to server and back to the client. The RTT includes packet-progation delays, packet-queuing delay and packet-processing delay

- HTTP非持续连接总响应时间大致为RTT+RTT+服务器传输HTML文件的时间。

- HTTP持续连接。

- 关于HTTP持续连接和非持续连接的问题：

  ![Pic07](https://raw.githubusercontent.com/JIAHONGZHANG/Computer-network/master/src/Pic07.png)

- HTTP请求报文

![Pic03](https://raw.githubusercontent.com/JIAHONGZHANG/Computer-network/master/src/Pic03.png)

​	第一行叫**请求行**（request line），后面的叫**首部行**（header line）。

- 请求行有三个字段：**方法字段**、**URL字段**和**HTTP版本字段**。方法字段包括GET、POST、HEAD、PUT和DELETE。
- 请求报文通用格式后面有个**实体体**（entity body）。使用GET方法时实体体为空，而使用POST方法时才使用该实体体。
- HTTP响应报文

![Pic04](https://raw.githubusercontent.com/JIAHONGZHANG/Computer-network/master/src/Pic04.png)

​	第一行叫**初始状态行**（status line），中间叫**首部行**（header line），最后叫**实体体**（entity body）。

- Date：首部行指示服务器产生并发送该响应报文的日期和时间，是服务器从它的文件系统中检索到该对象，插入到响应报文，并发送该报文的时间。

- cookie技术有四个组件：

  1. 在HTTP响应报文中的一个cookie首部行；
  2. 在HTTP请求报文中的一个cookie首部行；
  3. 在用户端系统中保留一个cookie文件；
  4. 位于web站点的一个后端数据库。

- **Web缓存器**（ Web cache）也叫**代理服务器**（proxy server），它是能够代表初始Web服务器来满足HTTP请求的网络实体。**Web 缓存器**是**内容分发网络**（Content Distribution Network, **CDN**）的一部分。

  具体CDN和web cache不同之处见 <https://www.quora.com/How-is-CDN-different-from-caching>

- 条件GET方法

  1. 请求报文使用GET方法；
  2. 请求报文中含有一个“If-Modified-Since:” 首部行。

- 文件传输协议（File Transfer Protocol, FTP）控制连接贯穿整个用户会话期间，但是会话中每一次传输文件都需要建立一个新的数据连接。

- 因特网电子邮箱系统有三个主要的组成部分：

  1. 用户代理（user agent）
  2. 邮件服务器（mail server）
  3. 简单邮件传输协议（Simple Mail Transfer Protocol, SMTP）

- SMTP整个过程（假设Alice想给Bob发送一封简单的ASCII报文）：

  1. Alice调用她的邮件代理程序并提供Bob的邮件地址，撰写报文，然后指示用户代理发送该报文；
  2. Alice的用户代理把报文发给她的邮件服务器，在那里该报文放在报文队列中；
  3. 运行在Alice的邮件服务器上的SMTP客户端发现报文队列中的该报文，它就创建一个到运行在Bob邮件服务器上的SMTP服务器的TCP连接；
  4. 在经过一些初始的SMTP握手后，SMTP客户通过该TCP连接发送Alice的报文；
  5. 在Bob的邮件服务器上SMTP的服务器接收到该报文。Bob的邮件服务器然后将该报文放入Bob的邮箱中；
  6. 在Bob方便的时候，他调用用户代理阅读该报文。

- SMTP、POP3、IMAP、HTTP

  ![Pic05](https://raw.githubusercontent.com/JIAHONGZHANG/Computer-network/master/src/Pic05.png)

  **邮件服务器和用户代理间连接为POP3、IMAP或者HTTP**，浏览器则为HTTP，其他邮件程序则为POP3或者IMAP。

- 域名系统（Domain Name System, DNS）的主要任务是**进行主机名到IP地址转换**的目录服务。

- DNS是：

  1. 一个由分层的DNS服务器（DNS server）实现的分布式数据库；
  2. 一个使得主机能够查询分布式数据库的应用层协议， DNS协议运行在UDP上，使用53号端口。

- 根DNS服务器、顶级域（DNS）服务器、权威DNS服务器、本地DNS服务器

  ![Pic06](https://raw.githubusercontent.com/JIAHONGZHANG/Computer-network/master/src/Pic06.png)

- DNS缓存

- 共同实现DNS分布式数据库的所有DNS服务器存储了**资源记录**（Resource Record, RR），RR提供了**主机名到IP地址的映射**。

- RR是一个包含（Name, Value, Type, TTL）的4元组。TTL是该记录的生存时间。

  1. 如果Type为A，则Name为主机名，Value为主机名对应的IP地址。因此，一个类型为A的资源记录了提供了标准的主机名到IP地址的映射；
  2. 如果Type为NS，则Name是一个域（如 .com），而Value是知道如何获得这个域中主机IP地址的权威DNS服务器的主机名；
  3. 如果Type为CNAME，则Value为别名为Name的主机对应的规范主机名。该记录能够向查询的主机提供一个主机名对应的规范主机名；
  4. 如果Type为MX，则Value是个别名为Name的邮件服务器的规范主机名。

- 权威DNS含有A记录，上层DNS则含有A记录和NS记录。

- CDN范例：

  ![Pic06](https://raw.githubusercontent.com/JIAHONGZHANG/Computer-network/master/src/Pic08.png)

- Time to distribute F to N clients using client-server approach

  $$D_{c-s}\ge max \{ {NF/u_s}{,F/d_{min}}\}$$

  F	file size F

  $$u_s$$	server upload capacity

  $$d_i$$	peer i download capacity 

  $$u_i$$	peer i upload capacity

- Time to distribute F to N clients using P2P approach

  $$D_{P2P}\ge max\{ {F/u_s},{F/d_{min},{NF/(u_s+\sum{u_i})}}\}$$

- **BitTorrent**是一种用于**文件分发**的流行**P2P协议**。参与一个特定文件的分发的所有对等方的集合被称为一个**洪流**（torrent）。在一个洪流中的对等方彼此下载等长度的**文件块**（chunk），典型的块长度为**256KB**。

- 每个洪流中具有一个基础设施结点，称为**追踪器**（tracker）。当一个对等方加入某个洪流中，它向追踪器**注册自己**，并**周期性**地通知追踪器它仍在洪流中。通过这种方式，追踪器**追踪**参与洪流中的对等方。

-  假设一个对等方Alice，她有很多个临近对等方。

  - 在任何给定的时间中，每个对等方将具有来自该文件的块子集，并且不同的对等方具有不同的子集。Alice周期性地（经TCP连接）询问每个临近对等方它们所具有的块列表。有了这个信息，Alice将对她当前还没有的块发出请求（TCP连接）

  - Alice需要作出两个决定：

    她应当从她的邻居请求哪些块？

    她应当向她请求块的哪些邻居发送？

    **最稀缺优先**（rarest first）技术：针对她没有的块在她邻居中决定**最稀缺的块**（最稀缺的块就是哪些在她的邻居中副本数量最少的块），并首先请求那些那些最稀缺的块。

    一报还一报（未理解）

- DHT（未补充）


## Capter 3

- 运输层协议为运行在不同主机上的应用进程之间提供了**逻辑通信**（logic communication）功能。从应用程序的角度看，通过逻辑通信，**运行不同进程的主机好像直接相连一样**；实际上，这些主机或许位于地球的两侧，通过许多路由器及多种不同类型的链路连接。

- 在发送端，运输层将从发送应用程序进程接收的报文转换成**运输层分层**，用因特网术语来讲该分组称为**运输层报文（segment）**。

- 在协议栈中，运输层刚好位于网络层之上。网络层提供了**主机之间**的逻辑通信，而运输层为运行在不同主机上的**进程之间**提供了逻辑通信。

- 运输层中的TCP和UDP最基本的责任是，将**两个端系统间的IP的交付服务**扩展为运行在端系统上的**两个进程之间的交付服务**，这种称为**运输层的多路复用**（transport-layer multiplexing）和**多路分解**（demultiplexing）。

  在接收端，运输层检查这些字段，标识出接收套接字，进而将报文段定向到该套接字，称为**多路分解**

  在源主机从不同套接字中收集数据块，并为每个数据块封装上首部信息从而生成报文段，然后将报文段传递到网络层，称为**多路复用**

- 运输层多路复用的要求

  - 套接字有**唯一标识符**
  - 每个报文段有**特殊字段**（**源端口号字段**source port number field和**目的端口号字段**destination port number field）来**指示该报文段所要交付到的套接字**

- 端口号是一个**16bit**的数，则其大小为$$0\sim2^{16}$$

  其中$$0\sim1023$$是**周知端口号**（well-known port number），是受到限制的，如HTTP（80），FTP（21）。

- UDP套接字是一个**二元组**来全面标识的，该二元组包括一个目的IP地址和一个目的端口号，两个一样了，则在一个套接字里面

  TCP套接字是一个**四元组**来标识的，包括源IP地址、源端口号、目的IP地址和目的端口号，四个一样了，则在一个套接字里面

- UDP只是做了运输协议能够做的最少的工作，除了复用/分解功能以及少量的差错检验外，他几乎没有对IP增加别的东西。使用UDP时，在发送报文段之前，发送端和接收端运输层实体间**没有握手**，正因为如此，UDP被称为**无连接的**。

- **DNS**是一个通常使用UDP应用层协议的例子。

- UDP相对于TCP的优势

  - 关于何时、发送什么数据的应用层控制更为精细
  - 无需建立连接
  - 无状态连接
  - 分组首部开销小

- 流行的因特网应用及其下面的运输协议

  |      应用      | 应用层协议 | 下面的运输协议 |
  | :------------: | :--------: | :------------: |
  |    电子邮件    |    SMTP    |      TCP       |
  |  远程终端访问  |   Telnet   |      TCP       |
  |      Web       |    HTTP    |      TCP       |
  |    文件传输    |    FTP     |      TCP       |
  | 远程文件服务器 |    NFS     |    通常UDP     |
  |   流式多媒体   |  通常专用  |    UDP或TCP    |
  |   因特网电话   |  通常专用  |    UDP或TCP    |
  |    网络管理    |    SNMP    |    通常UDP     |
  |  路由选择协议  |    RIP     |    通常UDP     |
  |    名字转换    |    DNS     |    通常UDP     |

- UDP报文段结构

  <img src="https://raw.githubusercontent.com/JIAHONGZHANG/Computer-network/master/src/Pic09.jpeg" width="200px" />

- UDP检验和

  - 发送方的UDP对报文段中的所有16比特字的和进行反码运算，最后结果为检验和
  - 接收方拿文段中的16比特字的和进行比较，如果最后为1111111111111111，则没有问题，否则溢出说明里面出现了改变，则回卷

- 数据可以通过一条可靠的信道传输。借助于可靠信道，传输数据比特就不会受到损坏或丢失，而且所有数据都是按照其发送数据进行交付。实现这种服务抽象是**可靠数据传输协议**（reliable data transfer protocol） 

  - rdt1.0（**经完全可靠信道的可靠数据传输**）
  - rdt2.0（多了**ACK**和**NACK**的rdt1.0）
  - rdt2.1（packet上面加了序号1和0的rdt2.0）
  - rdt2.2（**去掉NACK**改为在ACK上面加了序号1和0）
  - rdt3.0（加了**timeout timer**）

- rdt3.0是一个**停等协议**（stop-and-wait operation）。假设定义发送方（或通道）的利用率（utilization）为：发送方实际忙于将发送比特送进信道的那部分时间与发送时间之比，即
  $$
  U_{sender}={L/R\over{RTT+{L/R}}}
  $$
  这种方式利用率极低，为了解决利用率问题，使用**流水线**（pipelining）技术，即**不使用停等方式运行，允许发送方发送多个分组而无需确认等待**

  ![Pic10](https://raw.githubusercontent.com/JIAHONGZHANG/Computer-network/master/src/Pic10.png)

  流水线技术对可靠数据传输协议可带来如下影响：

  - **必须增加序号范围**，因为每个输送中的分组（不计算重传的）必须有一个唯一的序号，而且也许有多个传输中的未确认的分组
  - 协议的发送方和接收方两端也许必须**缓存多个分组**
  - 所需序号范围和对缓冲的要求取决于数据传输协议如何处理丢失、损坏及延时过大的分组。解决流水线的差错恢复有两种基本的方法：**回退N步**（Go-Back-N, GBN）和**选择重传**（Selective Repeat, SR）

- 回退N步动画 <https://media.pearsoncmg.com/aw/ecs_kurose_compnetwork_7/cw/content/interactiveanimations/go-back-n-protocol/index.html>


  ![Pic11](https://raw.githubusercontent.com/JIAHONGZHANG/Computer-network/master/src/Pic11.png)

- 回退N步的问题在于当窗口长度和带宽时延积都很大时，单个分组的差错就能够引起GBN重传大量的分组，许多分组没有必要重传，所以，**选择重传**（SR）协议通过让发送方仅重传那些**它怀疑在接收方出错（丢失或受损）的分组**而避免不必要的重传。

  ​