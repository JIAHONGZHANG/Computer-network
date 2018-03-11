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

  ​

  ​

  ​

  ​