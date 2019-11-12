from unittest import TestCase

from xsdata.models.elements import Attribute, Length, Restriction, SimpleType


class AttributeTests(TestCase):
    def test_property_real_type(self):
        obj = Attribute.build()
        self.assertEqual("xs:string", obj.real_type)

        obj.ref = "foo"
        self.assertEqual(obj.ref, obj.real_type)

        obj.type = "bar"
        self.assertEqual(obj.type, obj.real_type)

        obj.simple_type = SimpleType.build()
        self.assertEqual("xs:string", obj.real_type)

        obj.simple_type.restriction = Restriction.build(base="thug")
        self.assertEqual(obj.simple_type.restriction.base, obj.real_type)

    def test_property_real_name(self):
        obj = Attribute.build(ref="bar")
        self.assertEqual("bar", obj.real_name)

        obj.name = "foo"
        self.assertEqual("foo", obj.real_name)

        with self.assertRaises(NotImplementedError):
            Attribute.build().real_name

    def test_get_restrictions(self):
        obj = Attribute.build()
        self.assertDictEqual({}, obj.get_restrictions())

        obj.use = "required"
        expected = dict(required=1)
        self.assertDictEqual(expected, obj.get_restrictions())

        obj.simple_type = SimpleType.build(
            restriction=Restriction.build(length=Length.build(value=1))
        )
        expected.update(dict(length=1))
        self.assertDictEqual(expected, obj.get_restrictions())

    def test_property_extensions(self):
        obj = Attribute.build()
        self.assertEqual([], obj.extensions)
