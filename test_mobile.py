class TestMobile:
    def test_get_mobile_data(self, mobile):
        assert mobile.get_additional_info() == 'Brand: Apple, model: XR, RAM: 128'

    def test_get_mobile_price(self, mobile):
        mobile.ram = 2
        assert mobile.get_mobile_price == 10
