from cmd3.console import Console

print Console.color

print Console.theme

Console.warning("Warning")
Console.error("Error")
Console.info("Info")
Console.msg("msg")
Console.ok("Success")

Console.color = False

Console.error("Error")
