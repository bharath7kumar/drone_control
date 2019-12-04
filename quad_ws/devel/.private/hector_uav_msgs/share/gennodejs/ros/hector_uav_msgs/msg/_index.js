
"use strict";

let MotorPWM = require('./MotorPWM.js');
let RawImu = require('./RawImu.js');
let VelocityXYCommand = require('./VelocityXYCommand.js');
let PositionXYCommand = require('./PositionXYCommand.js');
let Compass = require('./Compass.js');
let RawMagnetic = require('./RawMagnetic.js');
let Supply = require('./Supply.js');
let HeightCommand = require('./HeightCommand.js');
let YawrateCommand = require('./YawrateCommand.js');
let ServoCommand = require('./ServoCommand.js');
let RC = require('./RC.js');
let Altimeter = require('./Altimeter.js');
let MotorStatus = require('./MotorStatus.js');
let AttitudeCommand = require('./AttitudeCommand.js');
let VelocityZCommand = require('./VelocityZCommand.js');
let RuddersCommand = require('./RuddersCommand.js');
let ThrustCommand = require('./ThrustCommand.js');
let ControllerState = require('./ControllerState.js');
let MotorCommand = require('./MotorCommand.js');
let RawRC = require('./RawRC.js');
let HeadingCommand = require('./HeadingCommand.js');
let LandingGoal = require('./LandingGoal.js');
let TakeoffActionFeedback = require('./TakeoffActionFeedback.js');
let TakeoffFeedback = require('./TakeoffFeedback.js');
let TakeoffActionResult = require('./TakeoffActionResult.js');
let LandingActionResult = require('./LandingActionResult.js');
let LandingAction = require('./LandingAction.js');
let TakeoffAction = require('./TakeoffAction.js');
let LandingActionFeedback = require('./LandingActionFeedback.js');
let PoseActionGoal = require('./PoseActionGoal.js');
let TakeoffResult = require('./TakeoffResult.js');
let PoseAction = require('./PoseAction.js');
let PoseResult = require('./PoseResult.js');
let TakeoffGoal = require('./TakeoffGoal.js');
let PoseActionResult = require('./PoseActionResult.js');
let PoseActionFeedback = require('./PoseActionFeedback.js');
let PoseFeedback = require('./PoseFeedback.js');
let LandingResult = require('./LandingResult.js');
let PoseGoal = require('./PoseGoal.js');
let LandingFeedback = require('./LandingFeedback.js');
let TakeoffActionGoal = require('./TakeoffActionGoal.js');
let LandingActionGoal = require('./LandingActionGoal.js');

module.exports = {
  MotorPWM: MotorPWM,
  RawImu: RawImu,
  VelocityXYCommand: VelocityXYCommand,
  PositionXYCommand: PositionXYCommand,
  Compass: Compass,
  RawMagnetic: RawMagnetic,
  Supply: Supply,
  HeightCommand: HeightCommand,
  YawrateCommand: YawrateCommand,
  ServoCommand: ServoCommand,
  RC: RC,
  Altimeter: Altimeter,
  MotorStatus: MotorStatus,
  AttitudeCommand: AttitudeCommand,
  VelocityZCommand: VelocityZCommand,
  RuddersCommand: RuddersCommand,
  ThrustCommand: ThrustCommand,
  ControllerState: ControllerState,
  MotorCommand: MotorCommand,
  RawRC: RawRC,
  HeadingCommand: HeadingCommand,
  LandingGoal: LandingGoal,
  TakeoffActionFeedback: TakeoffActionFeedback,
  TakeoffFeedback: TakeoffFeedback,
  TakeoffActionResult: TakeoffActionResult,
  LandingActionResult: LandingActionResult,
  LandingAction: LandingAction,
  TakeoffAction: TakeoffAction,
  LandingActionFeedback: LandingActionFeedback,
  PoseActionGoal: PoseActionGoal,
  TakeoffResult: TakeoffResult,
  PoseAction: PoseAction,
  PoseResult: PoseResult,
  TakeoffGoal: TakeoffGoal,
  PoseActionResult: PoseActionResult,
  PoseActionFeedback: PoseActionFeedback,
  PoseFeedback: PoseFeedback,
  LandingResult: LandingResult,
  PoseGoal: PoseGoal,
  LandingFeedback: LandingFeedback,
  TakeoffActionGoal: TakeoffActionGoal,
  LandingActionGoal: LandingActionGoal,
};
