// vim: set syntax=arduino:

const int CONN1_PIN = 2;
const int CONN2_PIN = 3;
const int CONN3_PIN = 4;
const int CONN4_PIN = 5;

const int NB_PINS = 4;

const int DELAY = 1000;

const int PINS[NB_PINS] = {CONN1_PIN, CONN2_PIN, CONN3_PIN, CONN4_PIN};

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
