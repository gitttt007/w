

Wazuh是一个用于威胁预防、检测和响应的开源平台，使用场景广泛包括但不局限于：入侵检测、日志数据分析、完整性检查、漏洞检测、配置评估、事故应变、合规、云安全、容器安全等；



**wazuh manager：**

> /var/ossec/etc/ossec.conf

**wazuh indexer：**

> /etc/wazuh-indexer/opensearch.yml

**Filebeat-OSS：**

> /etc/filebeat/filebeat.yml

**wazuh dashboard：**

> /etc/wazuh-dashboard/opensearch_dashboards.yml
>
> /usr/share/wazuh-dashboard/data/wazuh/config/wazuh.yml





/var/ossec/ruleset  # 自带规则库

<img src="picture/wazuh/image-20240219231959855.png" alt="image-20240219231959855" style="zoom:60%;" />

sudo vim /var/ossec/etc/ossec.conf  # 配置

> 简单的配置介绍：https://blog.csdn.net/weixin_54704770/article/details/132450063



### [Configuration assessment](https://documentation.wazuh.com/current/getting-started/use-cases/configuration-assessment.html)

<img src="picture/wazuh/image-20240220001511216.png" alt="image-20240220001511216" style="zoom:33%;" />



![image-20240219235546761](picture/wazuh/image-20240219235546761.png)

<img src="picture/wazuh/image-20240220003327470.png" alt="image-20240220003327470" style="zoom:60%;" />

```bash
rmmod cramfs
```

重启后可发现结果转变为Passed

![image-20240220001031846](picture/wazuh/image-20240220001031846.png)

### [Malware detection](https://documentation.wazuh.com/current/getting-started/use-cases/malware-detection.html)

<img src="picture/wazuh/image-20240220003816924.png" alt="image-20240220003816924" style="zoom:50%;" />

<img src="picture/wazuh/image-20240220004828720.png" alt="image-20240220004828720" style="zoom:50%;" />

规则：

<img src="picture/wazuh/image-20240220005041996.png" alt="image-20240220005041996" style="zoom:50%;" />

### [File integrity monitoring](https://documentation.wazuh.com/current/getting-started/use-cases/file-integrity.html)

<img src="picture/wazuh/image-20240220010925184.png" alt="image-20240220010925184" style="zoom:50%;" />

![image-20240220010841953](picture/wazuh/image-20240220010841953.png)

### [Threat hunting](https://documentation.wazuh.com/current/getting-started/use-cases/threat-hunting.html)

<img src="picture/wazuh/image-20240220012119557.png" alt="image-20240220012119557" style="zoom: 33%;" />



### 实际检测SQL注入的例子

> 参考：https://blog.csdn.net/weixin_53434577/article/details/132453405

安装apache

```bash
sudo apt install apache2
```

将以下行添加到wazuh-agent主机的/var/ossec/etc/ossec.conf`文件中。这允许 Wazuh 代理监控 Apache 服务器的访问日志

<img src="picture/wazuh/image-20240220210249296.png" alt="image-20240220210249296" style="zoom:60%;" />

```bash
systemctl restart wazuh-agent
```

配置完成，之后模拟客户端进行注入，服务端进行检测。

使用如下命令，在攻击端进行。

```bash
curl -XGET "http://192.168.142.133/users/?id=SELECT+*+FROM+users";
```

<img src="picture/wazuh/image-20240220211028018.png" alt="image-20240220211028018" style="zoom:50%;" />

查看apache日志：

<img src="picture/wazuh/image-20240220211823516.png" alt="image-20240220211823516" style="zoom:50%;" />

分析/var/log/apache2/access.log，可查看wazuh-server检测到SQL注入攻击：

<img src="picture/wazuh/image-20240220212046975.png" alt="image-20240220212046975" style="zoom:50%;" />





