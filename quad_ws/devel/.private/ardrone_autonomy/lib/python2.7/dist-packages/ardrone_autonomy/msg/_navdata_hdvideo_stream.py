# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ardrone_autonomy/navdata_hdvideo_stream.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class navdata_hdvideo_stream(genpy.Message):
  _md5sum = "1ba321578916df95f899ca2f5348f234"
  _type = "ardrone_autonomy/navdata_hdvideo_stream"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """Header header
float64 drone_time
uint16 tag
uint16 size
uint32 hdvideo_state
uint32 storage_fifo_nb_packets
uint32 storage_fifo_size
uint32 usbkey_size
uint32 usbkey_freespace
uint32 frame_number
uint32 usbkey_remaining_time

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
  __slots__ = ['header','drone_time','tag','size','hdvideo_state','storage_fifo_nb_packets','storage_fifo_size','usbkey_size','usbkey_freespace','frame_number','usbkey_remaining_time']
  _slot_types = ['std_msgs/Header','float64','uint16','uint16','uint32','uint32','uint32','uint32','uint32','uint32','uint32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,drone_time,tag,size,hdvideo_state,storage_fifo_nb_packets,storage_fifo_size,usbkey_size,usbkey_freespace,frame_number,usbkey_remaining_time

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(navdata_hdvideo_stream, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.drone_time is None:
        self.drone_time = 0.
      if self.tag is None:
        self.tag = 0
      if self.size is None:
        self.size = 0
      if self.hdvideo_state is None:
        self.hdvideo_state = 0
      if self.storage_fifo_nb_packets is None:
        self.storage_fifo_nb_packets = 0
      if self.storage_fifo_size is None:
        self.storage_fifo_size = 0
      if self.usbkey_size is None:
        self.usbkey_size = 0
      if self.usbkey_freespace is None:
        self.usbkey_freespace = 0
      if self.frame_number is None:
        self.frame_number = 0
      if self.usbkey_remaining_time is None:
        self.usbkey_remaining_time = 0
    else:
      self.header = std_msgs.msg.Header()
      self.drone_time = 0.
      self.tag = 0
      self.size = 0
      self.hdvideo_state = 0
      self.storage_fifo_nb_packets = 0
      self.storage_fifo_size = 0
      self.usbkey_size = 0
      self.usbkey_freespace = 0
      self.frame_number = 0
      self.usbkey_remaining_time = 0

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
      buff.write(_get_struct_d2H7I().pack(_x.drone_time, _x.tag, _x.size, _x.hdvideo_state, _x.storage_fifo_nb_packets, _x.storage_fifo_size, _x.usbkey_size, _x.usbkey_freespace, _x.frame_number, _x.usbkey_remaining_time))
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
      end += 40
      (_x.drone_time, _x.tag, _x.size, _x.hdvideo_state, _x.storage_fifo_nb_packets, _x.storage_fifo_size, _x.usbkey_size, _x.usbkey_freespace, _x.frame_number, _x.usbkey_remaining_time,) = _get_struct_d2H7I().unpack(str[start:end])
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
      buff.write(_get_struct_d2H7I().pack(_x.drone_time, _x.tag, _x.size, _x.hdvideo_state, _x.storage_fifo_nb_packets, _x.storage_fifo_size, _x.usbkey_size, _x.usbkey_freespace, _x.frame_number, _x.usbkey_remaining_time))
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
      end += 40
      (_x.drone_time, _x.tag, _x.size, _x.hdvideo_state, _x.storage_fifo_nb_packets, _x.storage_fifo_size, _x.usbkey_size, _x.usbkey_freespace, _x.frame_number, _x.usbkey_remaining_time,) = _get_struct_d2H7I().unpack(str[start:end])
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
_struct_d2H7I = None
def _get_struct_d2H7I():
    global _struct_d2H7I
    if _struct_d2H7I is None:
        _struct_d2H7I = struct.Struct("<d2H7I")
    return _struct_d2H7I
