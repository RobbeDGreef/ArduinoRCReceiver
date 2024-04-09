#include "ppm.h"

/* The serial connection info */
#define BAUDRATE      9600
#define SERIAL_CONFIG SERIAL_8N1 /* Means 8 bytes of data, no parity enabled and 1 stop bit */  

#define THROTTLE    3
#define ROLL        1
#define PITCH       2
#define YAW         4

/* Because the serial.write() only writes bytes */
void writeserial(uint16_t data)
{
    /* Standard big endian translate and write */
    Serial.write((data >> 8) & 0xFF);
    Serial.write(data & 0xFF);
}

void setup()
{
    /* Setting up serial */
    Serial.begin(BAUDRATE, SERIAL_CONFIG);

    ppm.begin(A0, false);
}

void loop()
{
    uint16_t throttle = ppm.read_channel(THROTTLE);
    uint16_t roll = ppm.read_channel(ROLL);
    uint16_t pitch = ppm.read_channel(PITCH);
    uint16_t yaw = ppm.read_channel(YAW);

    /* Sending a start byte first */
    Serial.write((char)0);
    writeserial(throttle);
    writeserial(roll);
    writeserial(pitch);
    writeserial(yaw);
}
