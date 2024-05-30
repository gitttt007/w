package main  
  
import (  
	"bytes"  
	"encoding/json"  
	"fmt"  
	"io/ioutil"  
	"log"  
	"net/http"  
)  
  
func main() {  
	// 百度搜索API的URL，注意：你需要使用百度提供的API接口，这里是一个示例URL  
	url := "https://www.baidu.com/s?"  
  
	// 准备POST请求的数据  
	postData := make(map[string]string)  
	postData["wd"] = "胡歌" // wd是百度搜索的关键字参数  
  
	// 将请求数据转换为JSON  
	jsonBytes, err := json.Marshal(postData)  
	if err != nil {  
		log.Fatal(err)  
	}  
  
	// 创建一个请求  
	req, err := http.NewRequest("POST", url, bytes.NewBuffer(jsonBytes))  
	if err != nil {  
		log.Fatal(err)  
	}  
  
	// 设置请求头  
	req.Header.Set("Content-Type", "application/json")  
  
	// 创建一个HTTP Client，并发起请求  
	client := &http.Client{}  
	resp, err := client.Do(req)  
	if err != nil {  
		log.Fatal(err)  
	}  
	defer resp.Body.Close()  
  
	// 读取响应内容  
	body, err := ioutil.ReadAll(resp.Body)  
	if err != nil {  
		log.Fatal(err)  
	}  
  
	// 打印响应内容  
	fmt.Println(string(body))  
}