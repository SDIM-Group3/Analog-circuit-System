void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  float v = analogRead(A0);
  float voltage = v * (5.00 / 1024.00);
  float mass=voltage*0.9453-0.3721;
  Serial.print(mass);
  Serial.println(" kg");
//  Serial.print(voltage);
//  Serial.println(" V");
    delay(500);
  }
