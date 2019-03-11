# 从Gogs迁移项目至GitLab

我以前使用的代码托管系统是[Gogs](https://gogs.io/)，近期我切换到了更知名的代码托管系统[GitLab](https://about.gitlab.com/)。因此，我需要将原来托管在Gogs实例上的项目迁移到GitLab实例。
GitLab中提供了一些迁移工具，其支持的平台如下图：
![](https://blog.nyan.im/wp-content/uploads/2019/03/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7-2019-03-11-%E4%B8%8B%E5%8D%8810.42.32.png)
其中，[Gitea](https://gitea.io/)是Gogs的一个分支版本，我试着通过Gitea选项从Gogs导入项目，虽然GitLab能够正常列出Gogs上的项目列表，但是在导入时则会引发500错误。

经阅读文档得知，Gogs和GitLab均提供了操作代码仓库的API。因此，我可以编写一个Python脚本来迁移项目。

### 实现
源代码：[https://github.com/nyanim/migrate-gogs-to-gitlab ](https://github.com/nyanim/migrate-gogs-to-gitlab)
#### 获取Gogs上的仓库列表
官方文档：[ docs-api/Repositories at master · gogs/docs-api ](https://github.com/gogs/docs-api/tree/master/Repositories)
在Gogs上使用`GET /user/repos`接口即可获得当前已认证用户（通过个人操作令牌认证）有权读取的所有仓库信息。其中我们需要的字段是
- `full_name`：形如user/repo的仓库全名
- `description`：仓库描述
- `clone_url`：HTTPS的仓库url

#### 导入仓库至GitLab
官方文档：[ Projects API | GitLab ](https://docs.gitlab.com/ee/api/projects.html#create-project)
在GitLab上使用`POST /projects`即可创建新仓库。我们需要传入如下的参数：
- `name`：仓库名称
- `description`：仓库描述
- `visibility`：设置仓库的可见性，可选的选项有`private`, `internal`及`public`
- `import_url`：包含个人操作令牌的Gogs仓库URL，形如[https://806f09c786f04bf8663hf02h9c4696ebf96bfb49@your.gogs.com/foo/bar.git](https://806f09c786f04bf8663hf02h9c4696ebf96bfb49@your.gogs.com/foo/bar.git)

### 使用
修改`sample.py`，填入Gogs及GitLab实例的URL，操作令牌及第30行的Gogs域名，并运行`sample.py`即可。

