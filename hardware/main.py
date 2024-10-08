import machine
import network
from machine import Pin, time_pulse_us
from utime import sleep_ms

class UltrasonicSensor:
    def __init__(self, trigger_pin, echo_pin, echo_timeout_us=1000000):
        self.echo_timeout_us = echo_timeout_us
        self.trigger = Pin(trigger_pin, mode=Pin.OUT)
        self.trigger(0)
        self.echo = Pin(echo_pin, mode=Pin.IN)

    def _send_pulse_and_wait(self):
        self.trigger(0)
        sleep_ms(500)
        self.trigger(1)
        sleep_ms(100)
        self.trigger(0)
        try:
            pulse_time = time_pulse_us(self.echo, 1, self.echo_timeout_us)
            if pulse_time < 0:
                MAX_RANGE_IN_CM = 500
                pulse_time = int(MAX_RANGE_IN_CM * 29.1)
            return pulse_time
        except OSError as ex:
            if ex.args[0] == 110:
                raise OSError('Out of range')
            raise ex

    def distance_mm(self):
        pulse_time = self._send_pulse_and_wait()
        mm = pulse_time * 100 // 582
        return mm

    def distance_cm(self):
        pulse_time = self._send_pulse_and_wait()
        cms = (pulse_time / 2) / 29.1
        return cms

us = UltrasonicSensor(trigger_pin=22, echo_pin=23, echo_timeout_us=1000000)

while True:
    distance_cm = round(us.distance_cm(), 2)
    print(f'Distance: {distance_cm} cm')
    sleep_ms(100)
