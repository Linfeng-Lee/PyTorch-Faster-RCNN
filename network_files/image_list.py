import torch


class ImageList(object):
    """
    :param
     tensors:Tensor
     image_sizes:list[tuple[int,int]]
    """

    def __init__(self, tensors, image_sizes):
        self.tensors = tensors
        self.image_sizes = image_sizes

    def to(self, device):
        cast_tensor = self.tensors.to(device)
        return ImageList(cast_tensor, self.image_sizes)
