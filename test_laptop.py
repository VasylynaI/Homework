class TestLaptop:
    def test_get_laptop_data(self, laptop):
        assert laptop.get_additional_info() == 'Brand: Lenovo, model: XP, RAM: 64'

    def test_get_transformer_info(self, laptop):
        laptop.transformer_laptop = True
        assert laptop.get_transformer_info() == 'Transformer laptop: True'
