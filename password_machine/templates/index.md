# Password Machine
Generate random passwords


## Default Settings
32 characters, mix of upper case, lower case, numbers, and web-safe special characters

<br>
## API
GET /random-password

**Description:** Returns a random password

**Parameters**

|Name|Type|Acceptable Values|Default|Description|
|:---|:---:|---|:---:|--|
|length|text|any whole number|32|number of characters long
|upper|text|true, false|true|use upper case characters
|lower|text|true, false|true|use lower case characters
|numbers|text|true, false|true|use numbers
|special|text|true, false|true|use web-safe special characters

**Example**

/random-password?length=32&upper=true&lower=true&numbers=true&special=true

<br>
## Give it a try