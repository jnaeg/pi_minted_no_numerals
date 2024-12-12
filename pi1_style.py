from pygments.style import Style
from pygments.token import (
    Keyword,
    Name,
    Comment,
    String,
    Error,
    Number,
    Operator,
    Generic,
    Whitespace,
)


class Pi1Style(Style):
    """
    A colorful style, inspired by the terminal highlighting style.
    """

    background_color = "#ffffff"

    styles = {
        # Whitespace: "#bbbbbb",
        Comment: "italic #5D5D54",
        Comment.Preproc: "noitalic #5D5D54",
        Comment.Special: "bold",
        Keyword: "bold #0000FF",
        Keyword.Pseudo: "nobold",
        Keyword.Type: "#6434A3",
        # Operator: "#000000",
        # Operator.Word: "bold #000000",
        Name: "#000000",
        # Name.Builtin: "#BA36A5",
        Name.Function: "#006699",
        # Name.Class: "bold #BA36A5",
        # Name.Namespace: "bold #BA36A5",
        # Name.Exception: "bold #BA36A5",
        Name.Variable: "#BA36A5",
        # Name.Constant: "#BA36A5",
        # Name.Label: "#BA36A5",
        # Name.Entity: "bold #BA36A5",
        # Name.Attribute: "#BA36A5",
        # Name.Tag: "bold #BA36A5",
        # Name.Decorator: "#BA36A5",
        String: "#007000",
        String.Doc: "italic",
        String.Interpol: "#007000",
        String.Escape: "bold #007000",
        String.Regex: "#007000",
        String.Symbol: "#007000",
        String.Other: "#007000",
        Number: "#D0372D",
        # Generic.Heading: "bold #003300",
        # Generic.Subheading: "bold #003300",
        # Generic.Deleted: "border:#CC0000 bg:#FFCCCC",
        # Generic.Inserted: "border:#00CC00 bg:#CCFFCC",
        # Generic.Error: "#FF0000",
        # Generic.Emph: "italic",
        # Generic.Strong: "bold",
        # Generic.Prompt: "bold #000099",
        # Generic.Output: "#AAAAAA",
        # Generic.Traceback: "#99CC66",
        Error: "bg:#FFAAAA #AA0000",
    }
