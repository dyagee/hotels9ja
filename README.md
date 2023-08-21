# Hotels9ja

 
# **Notice:**

There will be database migration from postgresql to mongodb, also a change of hosting; as such there maybe changes in the endpoints.

**Hotels9ja is an API** for getting hotels details across the 36 states and capital. The search is narrowed down to the most popular cities or towns within that state.

The hotels details is based on the information available on [hotels.ng](https://hotels.ng) website.

The purpose of this project is to help the community and make hotel and logging details available to travellers; so use API with caution in accordance with the legal terms data usage as  state on [hotels.ng ](https://hotels.ng/) website.


--- 

Check  `openapi` docs on all the available endpoints  [here.](https://hotels9jaapi-1-v2064706.deta.app/docs)

You can also check  the  `postman` documentation  [here.](https://documenter.getpostman.com/view/27619807/2s93m62hhJ)

--- 


## Created with:

![Framework](https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white)  

![Database](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)


![Python](https://img.shields.io/badge/Python-blue?style=for-the-badge&logo=python&logoColor=FFD43B)


## Also tested with: 

![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white)

![Sqlite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

---

## Usage/Examples

```python
import requests
import json


def formatted_print(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

city = input("Enter city: ")
price = input("Enter price: ")
url = f"https://hotels9jaapi-1-v2064706.deta.app/hotel/{city}/{price}/?skip=0&limit=10"

response = requests.get(f"{url}")
if response.status_code == 200:
    print("sucessfully fetched the data")
    formatted_print(response.json())
else:
    print(f"Hello person, there's a {response.status_code} error with your request")

```  

Code Editor Preferred: 

![VSCode](https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white) 

---





## API Reference

### Get all hotels

```http
  GET https://hotels9jaapi-1-v2064706.deta.app/hotels/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `skip` | `int` | *Default:0* |
| `limit` | `int` | *Default:100* |

<img src="https://content.pstmn.io/2083a8bc-bff8-43a6-9f68-a83f40413634/cGljdi4xX2FsbC5QTkc=" alt="screenshot all hotels" >  

This endpoint returns all the hotels available in the 36 states and capital. The default search param is set to limit 100

### Get hotel by id

```http
  GET https://hotels9jaapi-1-v2064706.deta.app/hotel/hotel_id/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `hotel_id`      | `string` | **Required**. *Id of item to fetch* |


<img src="https://content.pstmn.io/330db064-a335-4f89-b217-b89904863f8c/cGljdi4xX2lkLlBORw==" alt="screenshot hotel by id">

This endpoint gives hotel details based on the hotel_id passed. 


### Get hotels by State

```http
  GET https://hotels9jaapi-1-v2064706.deta.app/hotels/state/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `state`      | `string` | **Required**.|
| `skip`      | `int` | *Default:0*|
| `limit`      | `int` | *Default:50*|


<img src="https://content.pstmn.io/4418a6d5-e883-4379-b5ca-0ec84276e7c3/cGljdi4xX3N0YXRlLlBORw==" alt="screenshot hotel by state">

This endpoint returns all the hotels available in the specified state. The default search param is set to limit 50.

#### Get hotels by state and city

```http
  GET https://hotels9jaapi-1-v2064706.deta.app/hotels/state/city/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `state`      | `string` | **Required**.|
| `city`      | `string` | **Required**.|
| `skip`      | `int` | *Default:0*|
| `limit`      | `int` | *Default:50*|


<img src="https://content.pstmn.io/54324e76-f2fa-4e92-b10a-169e55f83edb/cGljdi4xX3N0YXRlX2NpdHkuUE5H" alt="screenshot hotel by state and city">

This endpoint returns all the hotels available in the specified state and city. The default search param is set to limit 50. 


#### Get hotels by state and price

```http
  GET https://hotels9jaapi-1-v2064706.deta.app/hotels/state/city/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `state`      | `string` | **Required**.|
| `price`      | `int` | **Required**.|
| `skip`      | `int` | *Default:0*|
| `limit`      | `int` | *Default:50*|


<img src="https://content.pstmn.io/845b5908-a3f6-4f14-acf0-c466cc522f8f/cGljdi4xX3N0YXRlX3ByaWNlLlBORw==" alt="screenshot hotel by state and price">

This endpoint returns all the hotels available in the specified state and price. It returns price less than or equal to the submitted price. The default search param is set to limit 50. 


#### Get hotels by city

```http
  GET https://hotels9jaapi-1-v2064706.deta.app/hotels/city/all/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `city`      | `string` | **Required**.|
| `skip`      | `int` | *Default:0*|
| `limit`      | `int` | *Default:50*|


<img src="https://content.pstmn.io/70eaa745-9a29-42b8-b689-ff3fdde75ea1/cGljdi4xX2NpdHlfYWxsLlBORw==" alt="screenshot hotel by city">

This endpoint returns all the hotels available in the specified city. The default search param is set to limit 50.

#### Get hotels by city and price

```http
  GET https://hotels9jaapi-1-v2064706.deta.app/hotel/city/price/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `city`      | `string` | **Required**.|
| `price`      | `int` | **Required**.|
| `skip`      | `int` | *Default:0*|
| `limit`      | `int` | *Default:50*|


<img src="https://content.pstmn.io/65f32f1d-10fc-4676-98d1-482b68134ec5/cGljdi4xX2NpdHlfcHJpY2UuUE5H" alt="screenshot hotel by city and price">

This endpoint returns all the hotels available in the specified city and price. Available hotels from the submitted price and below will be returned. The default search param is set to limit 50.

#### Get cheap hotels

```http
  GET https://hotels9jaapi-1-v2064706.deta.app/cheap/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `skip`      | `int` | *Default:0*|
| `limit`      | `int` | *Default:50*|

<img src="https://content.pstmn.io/34ea1d81-344a-4c68-acc5-f1f03ef07bd1/cGljdi4xX2NoZWFwLlBORw==" alt="screenshot cheap hotels">

This endpoint returns all the hotels available that the price is less than NGN 10,000. The default search param is set to limit 50.


#### Get affordable hotels

```http
  GET https://hotels9jaapi-1-v2064706.deta.app/moderate/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `skip`      | `int` | *Default:0*|
| `limit`      | `int` | *Default:50*|

<img src="https://content.pstmn.io/5ddeab14-21ce-4cc9-8771-0a6812576fea/cGljdi4xX21vZGVyYXRlLlBORw==" alt="screenshot affordable hotels">

This endpoint returns all the hotels within the price range of NGN 10,000 - NGN 20,000. The default search param is set to limit 50.

#### Get expensive hotels

```http
  GET https://hotels9jaapi-1-v2064706.deta.app/expensive/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `skip`      | `int` | *Default:0*|
| `limit`      | `int` | *Default:50*|

<img src="https://content.pstmn.io/b80c9c09-e2a7-4fb6-9cca-1d614794057b/cGljdi4xX2V4cGVuc2l2ZS5QTkc=" alt="screenshot expensive hotels">

This endpoint returns all the hotels available that the price is above NGN 20,000. The default search param is set to limit 50.


---


## Roadmap

- Add more hotels 

- Add more integrations 

- Deploy v2 to alternative cloud platform



## Feedback

If you have any feedback, please reach out to us at ageeaondo45@gmail.com

---

## Acknowledgements

 - [FastAPI with ORM Database ](https://fastapi.tiangolo.com/tutorial/sql-databases/#__tabbed_10_1)
 - [Deploy FastAPI to Deta Space](https://fastapi.tiangolo.com/deployment/deta/#__tabbed_1_2)