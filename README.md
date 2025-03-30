# pon
PON (**P**ython **O**bject **N**otation) is a lightwight text-based data-interchange format by and for Python programmers. 
It is:
  * human friendly (easy for humans to read and write)
  * machine friendly (easy for machines to parse and generate)
  * extensible
  * bateries-inclueded
  * programming-language-agnostic (but explicitly designed to be friendly to Python programmers)
  * relatively secure from common deserialization attacks (eval not used, pickle not used, etc)

The PON data-interchange format is heavily inspired by JSON (**J**ava**S**cript **O**bject **N**otation). We the creator's of PON believe that the broad success of JSON was not a mere accident but can actually be attributed to several of its design properties:

  * lightweight
  * readable
  * minimal
  * flexible (encode type info in the data itself, no explicit schemas required)
  * familiar and conventint to JavaScript programmers
  * limited and secure (less vulnerability to arbitrary remote code executions than other formats)

PON is "Python's answer to JSON". It aims to replicate the same great ideas of JSON into a purpose 
built data-interchange format for Python programs, while also adding a few ideas of its own to
create a more extensible data-interchange format.

Out of the box PON has the following 'standard types', that any PON compatible serializer 
and deserializer must support:

|PON Type | Description                                       |
|-------- | -----------                                       |
| str     | strings                                           |
| bytes   | bytes                                             |
| bool    | True or False                                     | 
| int     | integer (size limit deserializer dependent)       |
| float   | float (bit representation deserializer dependent) |
| Decimal | decimal                                           |
| None    | a None/Null value                                 |
| dict    | an unordered map of keys and values               |
| list    | an ordered list of values                         |
| tuple   | animmutable ordered list of values                |
| set     | an unordered collection of unique values          |
| Counter | an unordered collection of values                 |

exactly what kinds of data these objects deserialize into is a choice of the PON serailizer 
and deserializer implementor, but see below for the mapping of the refence Python implemention 
(this project):

|PON Type | Python Type         |
|-------- | -----------         |
| str     | str                 |
| bytes   | bytes               |
| bool    | bool                |
| int     | int                 |
| float   | float               |
| Decimal | decimal.Decimal     |
| None    | NoneType            |
| dict    | dict                |
| list    | list                |
| tuple   | tuple               |
| set     | set                 |
| Counter | collections.Counter |

In addition to these standard builtin types, PON has a notion of "extension" types. 
Extension types allow a PON document to include values with a type not present in 
the standard types. A serialzer can register a new type along with serialization 
logic to enable dumping new types in a PON document. A deserializer can register a new type
along with deserialization logic to enable parsing out new types in a PON document.

Care must be taken when adding extension types since it could present a possible attack vector. 
Users should stick to the standard types as much as possible, only introducing an extension type 
when it's really needed, and keep extension types simple. The "batteries included" philosophy 
should help here. PON makes adding them easy when you need to though.

Below is an example PON document describing an "order":

```
{
   "order_id": 1,
   "order_time": datetime(2025,1,1,0,0,tzinfo=None),
   "customer_id": 4 
   "items": [
      {
         "product_id": 1,
         "product_price_at_time_of_order: Decimal("9.99"),
         "number_of_items": 2,
         "tags": set([
            "food"
         ])
      }
   ]
}
```
