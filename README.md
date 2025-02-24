# DVC

## BUILD DVC
1) В DockerfileDVC заменить <bucket-name> на имя бакета с yandex-cloud
2) создать файл .env с полями `AWS_ACCESS_KEY_ID` и `AWS_SECRET_ACCESS_KEY`
3) ```bash
    docker-compose up
    ```
4)  При успешном билде 
    ```bash
    docker run -it --rm <image-name> bash
    ```

- Далее можно применять команды dvc(dvc pull, dvc add и т.д.)