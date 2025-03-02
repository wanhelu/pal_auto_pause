# pal_auto_pause
用于实现幻兽帕鲁服务端在无玩家在线时自动暂停的py脚本
## 功能介绍
定期查询服务器中在线玩家数，若连续10分钟无玩家在线则关闭服务端  
关闭服务端后监听端口，当收到连接请求时重新启动服务端
## 使用
*本脚本仅适用于windows版本的专用服务端*   
1. 将本脚本放置于PalServer.exe同一目录下
2. 配置帕鲁服务器，将*RESTAPIEnabled*选项设置为*True*
3. 修改本脚本中的*Authorization*信息为自己的密码所对应的密钥，可参考<https://docs.palworldgame.com/api/rest-api/info>
4. 运行本脚本  
