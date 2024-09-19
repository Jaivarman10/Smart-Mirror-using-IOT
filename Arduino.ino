int ledPin = 13;
String inputString = "";
void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
  inputString.reserve(200);
}
void loop() {
  if (Serial.available()) {
    char inChar = (char)Serial.read();
    inputString += inChar;
    if (inChar == '\n') {
      inputString.trim();
      if (inputString == "ON") {
        digitalWrite(ledPin, HIGH);
        Serial.println("LED is ON");
      }
      else if (inputString == "OFF") {
        digitalWrite(ledPin, LOW);
        Serial.println("LED is OFF");
      }
      inputString = "";
    }
  }
}
