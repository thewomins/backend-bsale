<h1 id="api-nombre-app-">Api Bsale v1.0.0</h1>

# Table of Contents

- [Table of Contents](#table-of-contents)
  - [Get Product](#get-product)
  - [Get all products](#get-all-products)
  - [Read all poducts in range](#read-all-poducts-in-range)
  - [Search products](#search-products)
  - [Get category by id](#get-category-by-id)
  - [Get all categories](#get-all-categories)
- [Schemas](#schemas)
  - [Category](#category)
  - [Product](#product)
  - [HTTPValidationError](#httpvalidationerror)
  - [ValidationError](#validationerror)

---

## Get Product

<a id="opIdread_product_products__product_id__get"></a>


`GET /products/{product_id}`

*Read Product by his id*

<h3 id="read_product_products__product_id__get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|product_id|path|integer|true|none|

> Example responses

> 200 Response

```json
{
  "name": "string",
  "url_image": "string",
  "price": 0,
  "discount": 0,
  "id": 0,
  "category": 0
}
```

<h3 id="read_product_products__product_id__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[Product](#schemaproduct)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|


## Get all products

<a id="opIdread_all_products_products_get"></a>



`GET /products`
`GET /products/?ids={id}&ids={id}`

*Read All Products*

<h3 id="read_all_products_products_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|ids|query|array[integer]|false|none|

> Example responses

> 200 Response

```json
[
  {
    "name": "string",
    "url_image": "string",
    "price": 0,
    "discount": 0,
    "id": 0,
    "category": 0
  }
]
```

<h3 id="read_all_products_products_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

## Read all poducts in range

<a id="opIdread_products_in_range_products_inrange__minimo___maximo___get"></a>


`GET /products/inrange/{minimo}-{maximo}/`
`GET /products/inrange/{minimo}-{maximo}/?ids={id}&ids={id}`

*Read Products In Range*

<h3 id="read_products_in_range_products_inrange__minimo___maximo___get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|minimo|path|integer|true|none|
|maximo|path|integer|true|none|
|ids|query|array[integer]|false|none|

> Example responses

> 200 Response

```json
[
  {
    "name": "string",
    "url_image": "string",
    "price": 0,
    "discount": 0,
    "id": 0,
    "category": 0
  }
]
```

<h3 id="read_products_in_range_products_inrange__minimo___maximo___get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

## Search products

<a id="opIdsearch_product_search_products__product_name__get"></a>

`GET /search/products/{product_name}`
`GET /search/products/{product_name-product_name1}`

*Search Product which containt the given keywords in her name field*

<h3 id="search_product_search_products__product_name__get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|product_name|path|string|true|none|

> Example responses

> 200 Response

```json
[
  {
    "name": "string",
    "url_image": "string",
    "price": 0,
    "discount": 0,
    "id": 0,
    "category": 0
  }
]
```

<h3 id="search_product_search_products__product_name__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

## Get category by id

`GET /category/{category_id}`

*Read Category*

<h3 id="read_category_category__category_id__get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|category_id|path|integer|true|none|

> Example responses

> 200 Response

```json
{
  "name": "string",
  "id": 0,
  "products": []
}
```

<h3 id="read_category_category__category_id__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[Category](#schemacategory)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|



## Get all categories

<a id="opIdread_all_categories_categories_get"></a>

`GET /categories-only`

*Read Categories*

> Example responses

> 200 Response

```json
[
  {
    "name": "string",
    "id": 0,
    "products": [] //always empty
  }
]
```

<h3 id="read_categories_categories_only_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

# Schemas

## Category

```json
{
  "name": "string",
  "id": 0,
  "products": []
}

```

## Product

```json
{
  "name": "string",
  "url_image": "string",
  "price": 0,
  "discount": 0,
  "id": 0,
  "category": 0
}

```

## HTTPValidationError

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

```


## ValidationError

```json
{
  "loc": [
    "string"
  ],
  "msg": "string",
  "type": "string"
}

```


