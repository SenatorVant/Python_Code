from gpiozero import RGBLED

# ---------------- SETUP ----------------
eye_led = RGBLED(red=3, green=5, blue=7)

robot_name = "Bob"


# ---------------- COMMAND ----------------
def get_command():
    return {
        "robot": "Bob",
        "features": {
            "eyes": {
                "set_rgb_eye_color": [255, 0, 0]
            }
        }
    }


# ---------------- HELPERS ----------------
def convert_rgb(rgb):
    return tuple([v / 255 for v in rgb])


# ---------------- CORE FUNCTION ----------------
def rgb_eye(rgb):
    r, g, b = convert_rgb(rgb)

    print(f"Eye Color -> R:{r} G:{g} B:{b}")

    eye_led.color = (r, g, b)


# ---------------- MAIN ----------------
def main():
    command = get_command()

    if command["robot"] != robot_name:
        print("Command not for this robot.")
        return

    eyes = command["features"]["eyes"]

    if "set_rgb_eye_color" in eyes:
        rgb = eyes["set_rgb_eye_color"]
        rgb_eye(rgb)


# ---------------- RUN ----------------
main()
