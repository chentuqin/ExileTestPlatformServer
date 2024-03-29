# ExileTestPlatformServer
# 放逐测试平台

### 前言
作者是前豌豆思维测试小弟，豌豆测试平台开发者，单人充当产品，设计，开发，测试，运维，内部运营推广等6个角色，旧测试平台就不在这里展示了。

因各种因素导致最后测试平台落地的结果并不理想，但在整个过程中受益匪浅并有所总结，而我还是想做出一个能让大部测试人员都认可并真正能提高工作效率的测试平台，从而有了这个放逐测试平台，既然不能服务于一个公司那么就流放到整个测试社区，让更多的测试人员对此平台进行检验，因此取名放逐。

### 项目文档
- 文档地址：https://github.com/yangyuexiong/ExileTestPlatformServer

### 项目介绍
`ExileTestPlatform`项目目前主要基于测试人员对测试用例配置环境，参数，变量，响应断言规则，数据库断言规则后，实施测试的接口测试平台(后续兼容UI测试)。

### 项目演示
- 前端项目地址：https://github.com/yangyuexiong/ExileTestPlatformWeb

- 项目演示地址：`待补充`

### 系统架构图
- 无法查看图片可以前往码云：https://gitee.com/yangyuexiong/ExileTestPlatformServer

![系统架构图](docs/ExileTestPlatform整体架构.png)

### 业务流程图
![业务流程图](docs/ExileTestPlatform业务流程.png)

### 数据库表设计
- [SQL文件：ExilicTestPlatform.sql](./docs/ExilicTestPlatform.sql)

![数据库表设计](docs/ExileTestPlatform数据库表设计.png)

### 后端技术
|技术|说明|官网|
|----------------------------------------|-------------------|---------------------------------------------- |
|Flask2.0|BIO MVC框架(2.0.2版本加入async异步)|https://flask.palletsprojects.com|
|Flask-SQLAlchemy|ORM|http://www.pythondoc.com/flask-sqlalchemy/quickstart.html|
|Flask-Migrate|Alembic处理Flask应用程序的SQLAlchemy数据库迁移|https://flask-migrate.readthedocs.io/en/latest|
|Flask-CORS|用于处理跨源资源共享(CORS)的Flask扩展，使跨源AJAX|https://pypi.org/project/Flask-Cors|
|PyMySQL|纯Python MySQL客户端库。PyMySQL的目标是成为MySQLdb的替代品，并在CPython、PyPy、IronPython和Jython上工作|https://pypi.org/project/PyMySQL/0.6.1|
|requests|Python HTTP库|https://docs.python-requests.org/en/latest/user/install|
|loguru|美化Python日志记录|https://pypi.org/project/loguru|
|Redis|缓存|https://redis.io|
|MySQl|关系型数据库|https://www.mysql.com|


### 前端技术
|技术|说明|官网|
|----------|--------------------- | -------------------------------------- |
|Vue3|前端框架|https://vuejs.org|
|Vue-router|路由框架|https://router.vuejs.org|
|Vuex|全局状态管理框架|https://vuex.vuejs.org|
|Element|前端UI框架|https://element.eleme.io|
|Axios|前端HTTP框架|https://github.com/axios/axios|
|v-charts|基于Echarts的图表框架|https://v-charts.js.org|
|Js-cookie|cookie管理工具|https://github.com/js-cookie/js-cookie|
|nprogress|进度条控件|https://github.com/rstacruz/nprogress|

### 项目结构
- 参考我的Flask最佳实践：https://github.com/yangyuexiong/Flask_BestPractices

### 接口清单

- [Postman文件](docs/ExilicTestPlatform.postman_collection.json)

|ID|接口名称|请求方式|功能描述|备注|
|---|--------------------|-----------|--------|--------|
|1|/api|GET|index|
|2|/api/tourist|GET|获取游客账号|
|3|/api/login|POST|登录|
|4|/api/login|DELETE|退出|
|5|/api/case_env/{id}|GET|测试环境详情  |
|6|/api/case_env|POST|新增测试环境  |
|7|/api/case_env|PUT|编辑测试环境  |
|8|/api/case_env|DELETE|删除测试环境  |
|9|/api/case/{id}|GET|用例详情  |
|10|/api/case|POST|新增用例|
|11|/api/case|PUT|编辑用例 |
|12|/api/case|DELETE|删除用例  |
|13|/api/case_scenario/{id}|GET|场景详情|
|14|/api/case_scenario|POST|新增场景例|
|15|/api/case_scenario|PUT|编辑场景|
|16|/api/case_scenario|DELETE|删除场景|
|17|/api/case_req_data/{id}|GET|获取用例Req数据|
|18|/api/case_req_data|POST|新增用例Req数据|
|19|/api/case_req_data|PUT|编辑用例Req数据|
|20|/api/case_req_data|DELETE|删除用例Req数据|
|21|/api/case_var/{id}|GET|变量详情|
|22|/api/case_var|POST|新增变量|
|23|/api/case_var|PUT|编辑变量|
|24|/api/case_var|DELETE|删除变量|
|25|/api/case_db/{id}|GET|用例数据库详情|
|26|/api/case_db|POST|新增用例数据|
|27|/api/case_db|PUT|编辑用例数据|
|28|/api/case_db|DELETE|删除用例数据|
|29|/api/resp_ass_rule/{id}|GET|获取请求响应断言规则明细|
|30|/api/resp_ass_rule|POST|新增请求响应断言规则明细|
|31|/api/resp_ass_rule|PUT|编辑请求响应断言规则明细|
|32|/api/resp_ass_rule|DELETE|删除请求响应断言规则明细|
|33|/api/field_ass_rule/{id}|GET|获取数据库字段断言规则明细|
|34|/api/field_ass_rule|POST|新增数据库字段断言规则明细|
|35|/api/field_ass_rule|PUT|编辑数据库字段断言规则明细|
|36|/api/field_ass_rule|DELETE|删除数据库字段断言规则明细|
|37|/api/case_bind_data|POST|用例绑定请求参数|
|38|/api/case_bind_data|PUT|用例解除绑定请求参数|
|39|/api/case_bind_resp_ass|POST|请求响应断言规则绑定|
|40|/api/case_bind_field_ass|POST|数据库字段断言规则绑定|
|41|/api/case_exec|POST|用例执行|根据参数控制
|42|/api/case_exec|POST|场景执行|根据参数控制
|43|/api/case_send|POST|调试请求|像Postman一样
|43|/api/rule_test|POST|取值规则调试|
|44|/api/case_page|POST|用例分页模糊查询|
|45|/api/case_var_page|POST|用例变量分页模糊查询|
|46|/api/resp_ass_rule_page|POST|返回值断言规则分页模糊查询|
|47|/api/field_ass_rule_page|POST|字段断言规则分页模糊查询|
|48|/api/case_req_data_page|POST|用例请求参数分页模糊查询|
|49|/api/case_env_page|POST|测试环境分页模糊查询|
|50|/api/case_db_page|POST|用例测试数据库分页模糊查询|
|51|/api/case_logs_page|POST|操作日志与执行日志分页模糊查询|
|52|/api/case_scenario_page|POST|用例场景分页模糊查询|

### 项目部署
- 前端：待补充
- 后端：参考我的Flask最佳实践：https://github.com/yangyuexiong/Flask_BestPractices