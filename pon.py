# Copyright 2025 Joseph P McAnulty. All rights reserved.
import base64 as _base64
import collections as _collections
import datetime as _datetime
import decimal as _decimal


# core exceptions ------------------------------------------------------
class PONEncodeError(Exception):
    """An exception raised when an object couldn't
    be PON encoded, generally because there is a bug
    or issue in one of the registered extension type encoders
    """
    pass


class PONDecodeError(Exception):
    """An exception raised when an object couldn't
    be PON decoded, usually because the encoded
    string is not syntactically valid, an unregistered
    extension type was encountered, or there was a bug
    or issue in one of the registered extension type decoders
    """
    pass


# core encoder class -------------------------------------------------------------
class PONEncoder:
    """
    A class for encoding Python objects to PON data. Exposes the dump and dumps methods,
    for performing the encoding. The register_extension_type_encoder method can be used to enable
    the dump and dumps methods on an object to encode more than just the standard PON types. 
    """
    def __init__(self):
        pass

    def dump(self, f, o, indent=None):
        """serialize Python object o to file f

        Args:
            - o: an object to serialize
            - f: a file-like object to write the serialized contents to
            - indent (int): an optional int specifying the number of 
                spaces to indent for "pretty printing". Values greater than
                0 turn on pretty printing, where 0 turns it off and uses 
                the most compact encoding possible (the default)

        Raises:
            - PONEncodeError: if the value couldn't be serialized

        """
        f.write(self.dumps(o, indent))

    def dumps(self, o, indent=None):
        """serialize Python object o to a string

        Args:
            - o: an object to serialize
            - indent (int): an optional int specifying the number of 
                spaces to indent for "pretty printing". Values greater than
                0 turn on pretty printing, where 0 turns it off and uses 
                the most compact encoding possible (the default)

        Returns:
            -str: o serialized to a string

        Raises:
            - PONEncodeError: if the value couldn't be serialized

        """
        pass

    def register_extension_type_encoder(self, ext_type, type_literal, encoder):
        """register an extension type encoder, to enable serialization of a new type.
        This function registers the extension type encoder at the module level, so future
        calls to the module level dump and dumps functions can leverage the encoder.

        Args:
            - type (type): The type who's values you want to make serializable
            - type_literal (str): the 'type_literal' to use in a PON doc to denote values of the registered type
            - encoder: a function-like object that takes a single value and returns a new value. This new value should be either some other registered extension type or on of the standard PON types

        """
        pass


# core decoder class ---------------------------------------------------------
class PONDecoder:
    """
    A class for decoding PON data to Python objects. Exposes the load and loads methods,
    for performing the decoding. The register_extension_type_decoder method can be used to enable
    the load and loads methods on a PONDecoder object to decode more than just the standard PON types.
    """
    def __init__(self):
        pass

    def load(self, f):
        """deserialize the contents of f to a Python object

        Args:
            - f: a file-like object containing a PON document

        Returns:
            - the deserialized object

        Raises:
            - PONDecodeError: if the value couldn't be deserialized

        """
        pass

    def loads(self, s):
        """deserialize string s to a Python object

        Args:
            - s (str): a PON document string

        Returns:
            - the deserialized object

        Raises:
            - PONDecodeError: if the value couldn't be deserialized

        """
        pass

    def register_extension_type_decoder(self, type_literal, decoder):
        """register an extension type decoder, to enable deserialization of a new type.
        This function only registers the extension type decoder at the PONDEcoder object
        it was called on.

        The decoder function passed should generally accept all arguments by using the
        (*args, **kwargs) function signature and return a single value, although this is 
        not a hard requiremnt.

        Args:
            - type_literal (str): the 'type_literal' who's values you want to make deserializable
            - decoder: a function-like object that takes args and kwargs and returns a new value.

        """
        pass


# module global funcs and supporting module private vars -------------------------------------------
_default_encoder = PONEncoder()
_default_decoder = PONDecoder()


def load(f):
    """deserialize the contents of f to a Python object

    Args:
        - f: a file-like object containing a PON document

    Returns:
        - the deserialized object

    Raises:
        - PONDecodeError: if the value couldn't be deserialized

    """
    return _default_decoder.load(f)


def loads(s):
    """deserialize string s to a Python object

    Args:
        - s (str): a PON document string

    Returns:
        - the deserialized object

    Raises:
        - PONDecodeError: if the value couldn't be deserialized

    """
    return _default_decoder.loads(s)


def dump(o, f, indent=None):
    """serialize Python object o to file f

    Args:
        - o: an object to serialize
        - f: a file-like object to write the serialized contents to
        - indent (int): an optional int specifying the number of 
            spaces to indent for "pretty printing". Values greater than
            0 turn on pretty printing, where 0 turns it off and uses 
            the most compact encoding possible (the default)

    Raises:
        - PONEncodeError: if the value couldn't be serialized

    """
    _default_encoder.dump(o, f, indent)


def dumps(o, indent=None):
    """serialize Python object o to a string

    Args:
        - o: an object to serialize
        - indent (int): an optional int specifying the number of 
            spaces to indent for "pretty printing". Values greater than
            0 turn on pretty printing, where 0 turns it off and uses 
            the most compact encoding possible (the default)

    Returns:
         -str: o serialized to a string

    Raises:
        - PONEncodeError: if the value couldn't be serialized

    """
    return _default_encoder.dumps(o, indent)


def register_extension_type_encoder(type, type_literal, encoder):
    """register an extension type encoder, to enable serialization of a new type.
    This function registers the extension type encoder at the module level, so future
    calls to the module level dump and dumps functions can leverage the encoder.

    Args:
        - type (type): The type who's values you want to make serializable
        - type_literal (str): the 'type_literal' to use in a PON doc to denote values of the registered type
        - encoder: a function-like object that takes a single value and returns a new value. This new value should be either some other registered extension type or on of the standard PON types

    """
    _default_encoder.register_extension_type(type, annotation, encoder)


def register_extension_type_decoder(type_literal, decoder):
    """register an extension type decoder, to enable deserialization of a new type.
    This function registers the extension type decoder at the module level, so future
    calls to the module level load and loads functions can leverage the decoder.

    Args:
        - type_literal (str): the 'type_literal' who's values you want to make deserializable
        - decoder: a function-like object that takes a single value and returns a new value.

    """
    _default_decoder.register_extension_type_decoder(type_literal, decoder)
