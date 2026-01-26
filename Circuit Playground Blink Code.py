#include <Adafruit_NeoPixel.h>

// Initialize the library
Adafruit_NeoPixel pixels(NUMPIXELS, PIN_NEOPIXEL, NEO_GRB + NEO_KHZ800);

void setup() {
  pixels.begin(); // Setup library
  pixels.setBrightness(50); // Set brightness (0-255)
}

void loop() {
  pixels.setPixelColor(0, pixels.Color(255, 0, 0)); // Set color to Red
  pixels.show(); // Display color
  delay(500); // Wait 500ms

  pixels.setPixelColor(0, pixels.Color(0, 0, 0)); // Turn off
  pixels.show(); // Display color
  delay(500); // Wait 500ms
}
