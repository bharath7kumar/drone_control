# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ardrone_autonomy/navdata_wind_speed.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class navdata_wind_speed(genpy.Message):
  _md5sum = "2cc5c1e9675c330dd38261e958a136d3"
  _type = "ardrone_autonomy/navdata_wind_speed"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """Header header
float64 drone_time
uint16 tag
uint16 size
float32 wind_speed
float32 wind_angle
float32 wind_compensation_theta
float32 wind_compensation_phi
float32 state_x1
float32 state_x2
float32 state_x3
float32 state_x4
float32 state_x5
float32 state_x6
float32 magneto_debug1
float32 magneto_debug2
float32 magneto_debug3

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id
"""
  __slots__ = ['header','drone_time','tag','size','wind_speed','wind_angle','wind_compensation_theta','wind_compensation_phi','state_x1','state_x2','state_x3','state_x4','state_x5','state_x6','magneto_debug1','magneto_debug2','magneto_debug3']
  _slot_types = ['std_msgs/Header','float64','uint16','uint16','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,drone_time,tag,size,wind_speed,wind_angle,wind_compensation_theta,wind_compensation_phi,state_x1,state_x2,state_x3,state_x4,state_x5,state_x6,magneto_debug1,magneto_debug2,magneto_debug3

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(navdata_wind_speed, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.drone_time is None:
        self.drone_time = 0.
      if self.tag is None:
        self.tag = 0
      if self.size is None:
        self.size = 0
      if self.wind_speed is None:
        self.wind_speed = 0.
      if self.wind_angle is None:
        self.wind_angle = 0.
      if self.wind_compensation_theta is None:
        self.wind_compensation_theta = 0.
      if self.wind_compensation_phi is None:
        self.wind_compensation_phi = 0.
      if self.state_x1 is None:
        self.state_x1 = 0.
      if self.state_x2 is None:
        self.state_x2 = 0.
      if self.state_x3 is None:
        self.state_x3 = 0.
      if self.state_x4 is None:
        self.state_x4 = 0.
      if self.state_x5 is None:
        self.state_x5 = 0.
      if self.state_x6 is None:
        self.state_x6 = 0.
      if self.magneto_debug1 is None:
        self.magneto_debug1 = 0.
      if self.magneto_debug2 is None:
        self.magneto_debug2 = 0.
      if self.magneto_debug3 is None:
        self.magneto_debug3 = 0.
    else:
      self.header = std_msgs.msg.Header()
      self.drone_time = 0.
      self.tag = 0
      self.size = 0
      self.wind_speed = 0.
      self.wind_angle = 0.
      self.wind_compensation_theta = 0.
      self.wind_compensation_phi = 0.
      self.state_x1 = 0.
      self.state_x2 = 0.
      self.state_x3 = 0.
      self.state_x4 = 0.
      self.state_x5 = 0.
      self.state_x6 = 0.
      self.magneto_debug1 = 0.
      self.magneto_debug2 = 0.
      self.magneto_debug3 = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_d2H13f().pack(_x.drone_time, _x.tag, _x.size, _x.wind_speed, _x.wind_angle, _x.wind_compensation_theta, _x.wind_compensation_phi, _x.state_x1, _x.state_x2, _x.state_x3, _x.state_x4, _x.state_x5, _x.state_x6, _x.magneto_debug1, _x.magneto_debug2, _x.magneto_debug3))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 64
      (_x.drone_time, _x.tag, _x.size, _x.wind_speed, _x.wind_angle, _x.wind_compensation_theta, _x.wind_compensation_phi, _x.state_x1, _x.state_x2, _x.state_x3, _x.state_x4, _x.state_x5, _x.state_x6, _x.magneto_debug1, _x.magneto_debug2, _x.magneto_debug3,) = _get_struct_d2H13f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_d2H13f().pack(_x.drone_time, _x.tag, _x.size, _x.wind_speed, _x.wind_angle, _x.wind_compensation_theta, _x.wind_compensation_phi, _x.state_x1, _x.state_x2, _x.state_x3, _x.state_x4, _x.state_x5, _x.state_x6, _x.magneto_debug1, _x.magneto_debug2, _x.magneto_debug3))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 64
      (_x.drone_time, _x.tag, _x.size, _x.wind_speed, _x.wind_angle, _x.wind_compensation_theta, _x.wind_compensation_phi, _x.state_x1, _x.state_x2, _x.state_x3, _x.state_x4, _x.state_x5, _x.state_x6, _x.magneto_debug1, _x.magneto_debug2, _x.magneto_debug3,) = _get_struct_d2H13f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_d2H13f = None
def _get_struct_d2H13f():
    global _struct_d2H13f
    if _struct_d2H13f is None:
        _struct_d2H13f = struct.Struct("<d2H13f")
    return _struct_d2H13f
