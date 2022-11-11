# Bsale test
Rest api of products for bsale store

## Built with

- **Python**
- **Fast api**

## API Reference

See [Documentation](docs.md)

## How to use?

 **`Important! you need to set the .env file before to test the app`**
### - With Docker

<dl>
  <dd>

Create the image
``` bash
docker build -t myimage .
```

Create and run the container
``` bash
docker run -d --name mycontainer -p 8000:8000 myimage
```

Open the app running on `http://127.0.0.1:8000/` or the interactive docs `http://127.0.0.1:8000/docs`
  </dd>
</dl>

<br />

### - Without Docker

<dl>
  <dd>
  
**`Requires Python >=3.10`**

Install dependencies
``` bash
pip install -r requirements.txt
```

Run the app
``` bash
uvicorn main:app --host 127.0.0.1 --port 8000
```

Open the app running on `http://127.0.0.1:8000/` or the interactive docs `http://127.0.0.1:8000/docs`

  </dd>
</dl>
