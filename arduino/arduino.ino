// vim: set syntax=arduino:

/*
 * General pins
 */
const int PIN_BOILER = 0;
const int PIN_POT = 1;

/*
 * Water pins
 */
const int PIN_4L = 2;
const int PIN_8L = 3;
const int PIN_12L = 4;

const int NB_WATER_PINS = 3;

const int WATER_PINS[NB_WATER_PINS] = { PIN_4L, PIN_8L, PIN_12L };

/*
 * Commands
 */
const char COMMAND_BREW_COFFEE[]    PROGMEM = "BREW DIS COFFEE PLZ";
const char COMMAND_POT_STATE[]      PROGMEM = "O HAI! I WAN MAH BUKKET ! U HAZ BUKKET ?";
const char COMMAND_WATER_QUANTITY[] PROGMEM = "I CAN HAZ MOAR WATER ?";
const char COMMAND_POT_PRESENCE[]   PROGMEM = "O HAI! I WAN MAH BUKKET ! U HAZ BUKKET ?";
const char COMMAND_STOP_BREWING[]   PROGMEM = "OUCH OUCH! TIZ COFFEE IZ HAWT! STOP!";

/*
 * Other constants
 */
const char NEWLINE = '\n';

/*
 *Global variables
 */
bool boilerOn = false;

/*
 * prototypes
 */
String readCommand();
boolean isCommand( String input, const char* command );


void setup() {
    Serial.begin(9600);
    Serial.println("booted");
}

void loop() {

    Serial.println("Waiting for command");
    String command = readCommand();
    Serial.println( command );
    boolean recognized = isCommand( command, COMMAND_POT_STATE );
    Serial.println( recognized );

}

String readCommand() {

    String command = "";
    bool endOfCommand = false;

    char in = '\0';

    while( !endOfCommand ) {

        while( Serial.available() ) {
            in = Serial.read();
            if( in == NEWLINE ) {
                endOfCommand = true;
            } else {
                command.concat(in);
            }
        }

    }

    return command;
}

boolean isCommand( String input, const char* command ) {

    byte pos = 0;
    boolean same = true;
    char character = (char)pgm_read_byte(command);

    while ( same && character != '\0' ) {

        same = ( character == input[pos] );

        command++;
        pos++;
        character = (char)pgm_read_byte(command);
    }

    return same;

}

