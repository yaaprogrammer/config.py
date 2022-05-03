# config.py

a simple configuration class

## Getting Started

1. install pyyaml

   ```bash
   pip install pyyaml
   ```

2. create config.yml

    ```yaml
    test:
        fruit:
            apple: 10
            banana: 4
        vegetable:
            carrot: 3
    ```

3. import Configuration

    ```python
    from config import Configuration
    ```

4. get properties

    ```python
    config = Configuration()
    apple = config.getProperty("test.fruit.apple")
    print(f"apple:{apple}")
    ```

5. set properties

   ```python
    config = Configuration()
    config.setProperty("test.fruit.apple", 50)
    apple = config.getProperty("test.fruit.apple")
    print(f"apple:{apple}")
   ```

6. create `config_custom.yml` override `config.yml`

   ```yaml
    test:
        fruit:
            apple: 30
   ```
