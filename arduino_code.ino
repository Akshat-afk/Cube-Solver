char val;

void setup()
{
    Serial.begin(19200);
    pinMode(LED_BUILTIN, OUTPUT);
}

void loop()
{
    if (Serial.available() > 0)
    {
        val = Serial.read();
        Serial.println(val);
        if (val == '1')
        {
            Serial.write("ON\n");
            digitalWrite(LED_BUILTIN, HIGH);
        }
        if (val == '0')
        {
            Serial.write("OFF\n");
            digitalWrite(LED_BUILTIN, LOW);
        }
    }
}