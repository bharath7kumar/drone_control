# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ardrone_autonomy/navdata_references.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class navdata_references(genpy.Message):
  _md5sum = "263b844b053f4a098c75c1c26a452911"
  _type = "ardrone_autonomy/navdata_references"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """Header header
float64 drone_time
uint16 tag
uint16 size
int32 ref_theta
int32 ref_phi
int32 ref_theta_I
int32 ref_phi_I
int32 ref_pitch
int32 ref_roll
int32 ref_yaw
int32 ref_psi
float32 vx_ref
float32 vy_ref
float32 theta_mod
float32 phi_mod
float32 k_v_x
float32 k_v_y
uint32 k_mode
float32 ui_time
float32 ui_theta
float32 ui_phi
float32 ui_psi
float32 ui_psi_accuracy
int32 ui_seq

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
  __slots__ = ['header','drone_time','tag','size','ref_theta','ref_phi','ref_theta_I','ref_phi_I','ref_pitch','ref_roll','ref_yaw','ref_psi','vx_ref','vy_ref','theta_mod','phi_mod','k_v_x','k_v_y','k_mode','ui_time','ui_theta','ui_phi','ui_psi','ui_psi_accuracy','ui_seq']
  _slot_types = ['std_msgs/Header','float64','uint16','uint16','int32','int32','int32','int32','int32','int32','int32','int32','float32','float32','float32','float32','float32','float32','uint32','float32','float32','float32','float32','float32','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,drone_time,tag,size,ref_theta,ref_phi,ref_theta_I,ref_phi_I,ref_pitch,ref_roll,ref_yaw,ref_psi,vx_ref,vy_ref,theta_mod,phi_mod,k_v_x,k_v_y,k_mode,ui_time,ui_theta,ui_phi,ui_psi,ui_psi_accuracy,ui_seq

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(navdata_references, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.drone_time is None:
        self.drone_time = 0.
      if self.tag is None:
        self.tag = 0
      if self.size is None:
        self.size = 0
      if self.ref_theta is None:
        self.ref_theta = 0
      if self.ref_phi is None:
        self.ref_phi = 0
      if self.ref_theta_I is None:
        self.ref_theta_I = 0
      if self.ref_phi_I is None:
        self.ref_phi_I = 0
      if self.ref_pitch is None:
        self.ref_pitch = 0
      if self.ref_roll is None:
        self.ref_roll = 0
      if self.ref_yaw is None:
        self.ref_yaw = 0
      if self.ref_psi is None:
        self.ref_psi = 0
      if self.vx_ref is None:
        self.vx_ref = 0.
      if self.vy_ref is None:
        self.vy_ref = 0.
      if self.theta_mod is None:
        self.theta_mod = 0.
      if self.phi_mod is None:
        self.phi_mod = 0.
      if self.k_v_x is None:
        self.k_v_x = 0.
      if self.k_v_y is None:
        self.k_v_y = 0.
      if self.k_mode is None:
        self.k_mode = 0
      if self.ui_time is None:
        self.ui_time = 0.
      if self.ui_theta is None:
        self.ui_theta = 0.
      if self.ui_phi is None:
        self.ui_phi = 0.
      if self.ui_psi is None:
        self.ui_psi = 0.
      if self.ui_psi_accuracy is None:
        self.ui_psi_accuracy = 0.
      if self.ui_seq is None:
        self.ui_seq = 0
    else:
      self.header = std_msgs.msg.Header()
      self.drone_time = 0.
      self.tag = 0
      self.size = 0
      self.ref_theta = 0
      self.ref_phi = 0
      self.ref_theta_I = 0
      self.ref_phi_I = 0
      self.ref_pitch = 0
      self.ref_roll = 0
      self.ref_yaw = 0
      self.ref_psi = 0
      self.vx_ref = 0.
      self.vy_ref = 0.
      self.theta_mod = 0.
      self.phi_mod = 0.
      self.k_v_x = 0.
      self.k_v_y = 0.
      self.k_mode = 0
      self.ui_time = 0.
      self.ui_theta = 0.
      self.ui_phi = 0.
      self.ui_psi = 0.
      self.ui_psi_accuracy = 0.
      self.ui_seq = 0

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
      buff.write(_get_struct_d2H8i6fI5fi().pack(_x.drone_time, _x.tag, _x.size, _x.ref_theta, _x.ref_phi, _x.ref_theta_I, _x.ref_phi_I, _x.ref_pitch, _x.ref_roll, _x.ref_yaw, _x.ref_psi, _x.vx_ref, _x.vy_ref, _x.theta_mod, _x.phi_mod, _x.k_v_x, _x.k_v_y, _x.k_mode, _x.ui_time, _x.ui_theta, _x.ui_phi, _x.ui_psi, _x.ui_psi_accuracy, _x.ui_seq))
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
      end += 96
      (_x.drone_time, _x.tag, _x.size, _x.ref_theta, _x.ref_phi, _x.ref_theta_I, _x.ref_phi_I, _x.ref_pitch, _x.ref_roll, _x.ref_yaw, _x.ref_psi, _x.vx_ref, _x.vy_ref, _x.theta_mod, _x.phi_mod, _x.k_v_x, _x.k_v_y, _x.k_mode, _x.ui_time, _x.ui_theta, _x.ui_phi, _x.ui_psi, _x.ui_psi_accuracy, _x.ui_seq,) = _get_struct_d2H8i6fI5fi().unpack(str[start:end])
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
      buff.write(_get_struct_d2H8i6fI5fi().pack(_x.drone_time, _x.tag, _x.size, _x.ref_theta, _x.ref_phi, _x.ref_theta_I, _x.ref_phi_I, _x.ref_pitch, _x.ref_roll, _x.ref_yaw, _x.ref_psi, _x.vx_ref, _x.vy_ref, _x.theta_mod, _x.phi_mod, _x.k_v_x, _x.k_v_y, _x.k_mode, _x.ui_time, _x.ui_theta, _x.ui_phi, _x.ui_psi, _x.ui_psi_accuracy, _x.ui_seq))
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
      end += 96
      (_x.drone_time, _x.tag, _x.size, _x.ref_theta, _x.ref_phi, _x.ref_theta_I, _x.ref_phi_I, _x.ref_pitch, _x.ref_roll, _x.ref_yaw, _x.ref_psi, _x.vx_ref, _x.vy_ref, _x.theta_mod, _x.phi_mod, _x.k_v_x, _x.k_v_y, _x.k_mode, _x.ui_time, _x.ui_theta, _x.ui_phi, _x.ui_psi, _x.ui_psi_accuracy, _x.ui_seq,) = _get_struct_d2H8i6fI5fi().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_d2H8i6fI5fi = None
def _get_struct_d2H8i6fI5fi():
    global _struct_d2H8i6fI5fi
    if _struct_d2H8i6fI5fi is None:
        _struct_d2H8i6fI5fi = struct.Struct("<d2H8i6fI5fi")
    return _struct_d2H8i6fI5fi
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
