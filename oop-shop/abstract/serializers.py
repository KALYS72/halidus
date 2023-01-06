class BaseSerializer:
    class Meta:
        fields = []
        objects = []

    def serialize_obj(self, obj):
        representaiton = {}
        for field in self.Meta.fields:
            data = getattr(obj, field)
            representaiton[field] = data
        return representaiton
    
    def serialize_objects(self):
        representaiton = []
        for obj in self.Meta.objects:
            obj_repr = self.serialize_obj(obj)
            representaiton.append(obj_repr)
        return representaiton