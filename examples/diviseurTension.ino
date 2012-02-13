const int PIN_WATER = 0;

typedef int range_max;

const range_max NO_WATER = 50;
const range_max LITRE_1 = 200;
const range_max LITRE_4 = 250;
const range_max LITRE_8 = 300;
const range_max LITRE_12 = 400;

void setup()
{
  Serial.begin(9600);          //  setup serial
  pinMode(PIN_WATER, INPUT); 
}

void loop()
{
  int val = analogRead(PIN_WATER);
  Serial.println(val);
  Serial.print(" ");
  if(val <= NO_WATER) {
    Serial.println("Pas d'eau");
  } else if(val <= LITRE_1) {
    Serial.println("1 litre");
  } else if(val <= LITRE_4) {
    Serial.println("4 litres");
  } else if(val <= LITRE_8) {
    Serial.println("8 litres");
  } else if(val <= LITRE_12) {
    Serial.println("12 litres");
  }
}
