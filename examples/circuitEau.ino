// vim: set syntax=arduino:

const int LITER2_PIN = 2;
const int LITER4_PIN = 3;
const int LITER6_PIN = 4;
const int LITER8_PIN = 5;

const int NB_PINS = 4;

const int DELAY = 1000;

const int PINS[NB_PINS] = {LITER2_PIN, LITER4_PIN, LITER6_PIN, LITER8_PIN};

void setup() {

    Serial.begin(9600);
    for( int i = 0; i < NB_PINS; i++ ) {
        pinMode( PINS[i], INPUT );
    }

    Serial.println("booted");

}

void loop() {

    Serial.println("Readout:");
    for( int i = 0; i < NB_PINS; i++ ) {

        Serial.print("Pin ");
        Serial.print(i);
        Serial.print(" : ");

        boolean on = digitalRead( PINS[i] );
        Serial.println( on );

    }

    delay( DELAY );

}
