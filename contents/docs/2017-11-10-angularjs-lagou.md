

Angularjs

开发过程

效果图->搭建项目->分模块开发->产品->扩展

# 准备

## 搭建开发环境

### 编辑器：atom

### 调试工具：batarang

batarang

### Node.js

淘宝NPM镜像 http://npm.taobao.org

https://nodejs.org/en/download/

下载解压设置path路径

node-v8.9.1-win-x64.zip

```shell
# 查看版本
node -v
npm -v

# 用这个淘宝镜像，安装插件比较快
npm i -g cnpm
npm install -g cnpm --registry=https://registry.npm.taobao.org

cnpm -v
```

离线安装

```shell
# 下载
# https://registry.npmjs.org/npm/-/npm-5.5.1.tgz

# 执行
npm i -g npm-5.5.1.tgz
```

### 第三方依赖管理工具：bower

bower https://bower.io

安装

```shell
cnpm i -g bower

bower -v
```

配置文件----演示这两个配置文件的使用

.bowerrc 修改安装目录

bower.json 管理第三方依赖

### 代码管理工具：git

Git

### css预编译处理：less

http://lesscss.cn

在线less编译器 http://tool.oschina.net/less

常用语法：定义变量、后代选择器、文件引用 、函数

```less
// 定义变量
@bg_color:#000;
@bg_color

// 定义变量

// 后代选择器

// 文件引用 

// 函数

```

### 自动化构建工具：gulp

gulp  http://www.gulpjs.com.cn

优点：基于流、任务化

常用API：src、dest、watch、task、pipe

安装

```shell
cnpm i -g gulp
```





## Angular概念

module-----魔法书

directive------召唤魔法

service------攻击魔法

filter------其他魔法

controller------辅助魔法

### 单页应用

定义：页面跳转无刷新

方法：利用路由控制”页面“跳转

优点：页面切换流畅、前后端分分离

## 目录结构说明

bower_components：第三方依赖默认安装路径

src：源码

build：构建代码编译之后

dist：压缩后的

node_modules：

test：

## 小技巧

创建以点开头的文件及文件夹

```shell
echo ''>.file
touch .file

mkdir .folder
```

# 实际操作

## bower管理依赖

### angular模块

```shell
# 创建并切换到开发目录
cd E:\git_home\webSamples\webapp

# 创建bower配置文件
bower init
# 说明
# name --- webapp
# keywords --- angularjs

# 安装angular
bower install --save angular
# 说明
# --save 保存到配置文件

# 切换版本
bower install --save angular#1.2
```

**实验配置文件**

.bowerrc 修改安装目录

```shell
# 添加配置文件
touch .bowerrc

# 配置文件内容
{
"directory": "lib"
}

# 测试，再次安装一个依赖
bower install --save requirejs
# 说明
# 现在安装的依赖统一安在了lib目录下了
# 还会把以前安装的依赖统一复制到该路径下
# 默认安装在bower_components

# 删除依赖
bower uninstall requirejs
```

### 其他模块

```shell
bower install --save ui-router

bower install --save ngCookies validation ngAnimate
```



## gulp自动化构建

### 添加gulp模块

```shell
# 初始化配置文件
npm init

# node添加模块
cnpm i --save-dev gulp

# 批量添加其他模块
cnpm i --save-dev gulp-clean gulp-concat gulp-connect gulp-cssmin gulp-imagemin gulp-less gulp-load-plugins gulp-plumber gulp-uglify open
```

### 编写自动化脚本

gulpfile.js

```js
var gulp = require('gulp');
var $ = require('gulp-load-plugins');
var open = require('open');

var app = {
	srcPath: 'src/',
	devPath: 'build/',
	prdPath: 'dist/',
}

gulp.task('lib', function(){
	gulp.src('bower_components/**/*.js') // 读取文件
	.pipe(gulp.dest(app.devPath + 'vendor'))
	.pipe(gulp.dest(app.prdPath + 'vendor'));
});
```

执行

```shell
gulp lib
```

# 开发

## 模块划分



# 遇到的问题

1. 如下 

   ```shell
   E:\git_home\samples\angular_lagou>gulp lib
   module.js:538
       throw err;
       ^

   Error: Cannot find module 'orchestrator'
       at Function.Module._resolveFilename (module.js:536:15)
       at Function.Module._load (module.js:466:25)
       at Module.require (module.js:579:17)
       at require (internal/module.js:11:18)
       at Object.<anonymous> (E:\git_home\samples\angular_lagou\node_modules\_gulp@3.9.1@gulp\index.js:4:20)
       at Module._compile (module.js:635:30)
       at Object.Module._extensions..js (module.js:646:10)
       at Module.load (module.js:554:32)
       at tryModuleLoad (module.js:497:12)
       at Function.Module._load (module.js:489:3)
   ```

   解决：把node_modules删除，再重新安装一遍









































