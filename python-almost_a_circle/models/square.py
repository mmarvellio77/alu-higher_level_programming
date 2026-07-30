#!/usr/bin/python3
"""Square class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square.

        Args:
            size: size of square (width and height)
            x: x position
            y: y position
            id: instance id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return string representation."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    @property
    def size(self):
        """Get size."""
        return self.width

    @size.setter
    def size(self, value):
        """Set size."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes with args or kwargs."""
        if args and len(args) > 0:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if attrs[i] == "size":
                    self.size = arg
                else:
                    setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y,
        }
