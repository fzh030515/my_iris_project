This project is a machine learning application (irises classifier) that demonstrates the complete DevOps/MLOps process, including version control (Git, DVC), CI/CD (GitHub Actions), containerization (Docker), and experiment tracking (MLflow).

本项目是一个机器学习应用（鸢尾花分类器），演示完整的 DevOps/MLOps 流程，包括版本控制（Git、DVC）、CI/CD（GitHub Actions）、容器化（Docker）和实验跟踪（MLflow）。

The code for this project follows an automated pipeline from submission to production environment to ensure reliability and quality:
本项目的代码从提交到生产环境遵循自动化流水线，确保可靠性和质量：

1. Commit: 
   - Developers commit code changes on feature branches (e.g.`feature/train-model'). 
   - Before submission, it is recommended to run tests (`pytest`) and code checks (`black`) locally. 
1. Commit（提交）：
   - 开发者在功能分支（如 `feature/train-model`）上提交代码更改。
   - 提交前，建议本地运行测试（`pytest`）和代码检查（`black`）。

2. Build: 
   - GitHub Actions automatically trigger build jobs when code is merged into an integration branch (such as `dev`) via a Pull Request (PR). 
   - Construction includes: 
     - Pull code and DVC-managed data (run `dvc pull` to get the dataset). 
     - Build Docker images (lightweight images based on Dockerfile). 
2. Build（构建）：
   - 当代码通过 Pull Request（PR）合并到集成分支（如 `dev`）时，GitHub Actions 自动触发构建作业。
   - 构建包括：
     - 拉取代码和 DVC 管理的数据（运行 `dvc pull` 获取数据集）。
     - 构建 Docker 镜像（基于 `Dockerfile` 的轻量级镜像）。

3. Test: 
   - Run test phase immediately after build: 
     - Unit tests: Perform pytest tests (including model training and data loading tests) in the `tests/` directory. 
     - Code checking: Verify the code format using `black`. 
     - If the test fails, the pipeline aborts and PR cannot merge. 
3. Test（测试）：
   - 构建后立即运行测试阶段：
     - 单元测试：执行 `tests/` 目录下的 pytest 测试（包括模型训练和数据加载测试）。
     - 代码检查：使用 `black` 验证代码格式。
     - 如果测试失败，流水线中止，PR 无法合并。

4. Staging (pre-production): 
   - When code is merged into the staging branch, it is automatically deployed to a pre-production environment (such as a mock server). 
   - In this environment: 
     - Run integration tests to verify how the model interacts with external services. 
     - Model performance metrics such as accuracy are checked via MLflow. 
4. Staging（预生产）：
   - 代码合并到 `staging` 分支后，自动部署到预生产环境（如模拟服务器）。
   - 在此环境中：
     - 运行集成测试，验证模型与外部服务的交互。
     - 通过 MLflow 检查模型性能指标（如准确率）。

5. Prod (Production): 
   - Eventually, code is automatically deployed to production when it is merged from the staging branch to the main branch. 
   - include: 
     - Push Docker images to image repositories (e.g. Docker Hub). 
     - Update production applications (e.g., via cloud service deployment). 
     - Monitor model performance in production environments. 
5. Prod（生产）：
   - 最终，代码从 `staging` 合并到 `main` 分支时，自动部署到生产环境。
   - 包括：
     - 推送 Docker 镜像到镜像仓库（如 Docker Hub）。
     - 更新生产应用（例如，通过云服务部署）。
     - 监控生产环境中的模型表现。

The entire process is automated through GitHub Actions, reducing manual intervention. For detailed configuration, see [.github/workflows/ci-cd.yml](.github/workflows/ci-cd.yml). 
整个流程通过 GitHub Actions 自动化，减少人工干预。详细配置见 [.github/workflows/ci-cd.yml](.github/workflows/ci-cd.yml)。

This project uses the Git branching strategy, where different branches trigger specific CI/CD pipelines. The rules are as follows: 
本项目使用 Git 分支策略，不同分支触发特定的 CI/CD 管道。规则如下：

| branch type| trigger condition| pipe action| goal| 
|----------|-----------|-----------|-------| 
| **feature/**   |Run basic tests and builds| Verify new features without deploying| Verify new features without deploying  | 
| **dev** |Push code or PR merge into dev| Run full tests, builds, and code reviews| Integrated functionality, ready for pre-release| 
| **staging** |Push code or PR merged into staging| Run tests and deploy to pre-production| simulated production test| 
| **main** |Push code or PR merged into `main`(protected)| Run all tests and deploy to production| release officially| 

| 分支类型 | 触发条件 | 管道动作 | 目的 |
|----------|-----------|-----------|-------|
| **feature/** | 创建 PR 指向 `dev` 分支 | 运行基本测试和构建 | 验证新功能，不部署 |
| **dev** | 推送代码或 PR 合并到 `dev` | 运行完整测试、构建和代码检查 | 集成功能，准备预发布 |
| **staging** | 推送代码或 PR 合并到 `staging` | 运行测试并部署到预生产环境 | 模拟生产测试 |
| **main** | 推送代码或 PR 合并到 `main`（受保护） | 运行所有测试并部署到生产 | 正式发布 |

Pipeline configuration is based on GitHub Actions events (see [CI/CD Configuration](.github/workflows/ci-cd.yml)), ensuring that only compliant code gets into production.

管道配置基于 GitHub Actions 事件（见 [CI/CD 配置](.github/workflows/ci-cd.yml)），确保只有合规代码能进入生产。

Project Quick Start-Install 

-dependencies: `pip install -r requirements.txt`

-Run training: `python src/main.py--data-version v1`

-View MLflow experiments: `mlflow ui`

项目快速开始
- 安装依赖：`pip install -r requirements.txt`
- 运行训练：`python src/main.py --data-version v1`
- 查看 MLflow 实验：`mlflow ui`




