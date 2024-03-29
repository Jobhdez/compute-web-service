
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BEGIN DEFINE EQ EQQ EXCLAMATION FALSE GREATER GREATEREQ IF INTEGER LAMBDA LESS LESSEQ LET LPAREN MINUS MUL NAME NOT OR PLUS RPAREN SET TRUE WHILEexpressions : expression expressionsexpressions : expressionexpression : INTEGERexpression : TRUE\n                  | FALSEexpression : LPAREN op expression expression RPARENexpression : NAMEexpression : LPAREN IF expression expression expression RPARENexpression : LPAREN WHILE expression expression RPARENexpression : LPAREN SET EXCLAMATION expression expression RPARENexpression : LPAREN LET binding expressions RPARENexpression : LPAREN BEGIN expressions RPARENexpression : LPAREN expressions RPARENop : PLUS\n        | MUL\n        | MINUS\n        | AND\n        | OR\n        | EQ\n        | LESS\n        | LESSEQ\n        | GREATER\n        | GREATEREQ\n        | NOTbinding : LPAREN LPAREN NAME expression RPAREN RPARENexpression : LPAREN DEFINE expression expression RPARENexpression : LPAREN LAMBDA LPAREN params RPAREN expression RPARENparams : NAME paramsparams : NAME'
    
_lr_action_items = {'INTEGER':([0,2,3,4,5,6,7,9,10,11,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,35,37,40,42,45,49,51,53,54,55,56,58,59,63,64,],[3,3,-3,-4,-5,3,-7,3,3,3,3,3,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,3,3,3,3,3,-13,3,3,3,-12,-6,-9,3,-11,-26,3,-8,-10,-27,-25,]),'TRUE':([0,2,3,4,5,6,7,9,10,11,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,35,37,40,42,45,49,51,53,54,55,56,58,59,63,64,],[4,4,-3,-4,-5,4,-7,4,4,4,4,4,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,4,4,4,4,4,-13,4,4,4,-12,-6,-9,4,-11,-26,4,-8,-10,-27,-25,]),'FALSE':([0,2,3,4,5,6,7,9,10,11,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,35,37,40,42,45,49,51,53,54,55,56,58,59,63,64,],[5,5,-3,-4,-5,5,-7,5,5,5,5,5,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,5,5,5,5,5,-13,5,5,5,-12,-6,-9,5,-11,-26,5,-8,-10,-27,-25,]),'LPAREN':([0,2,3,4,5,6,7,9,10,11,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,40,42,45,49,51,53,54,55,56,58,59,63,64,],[6,6,-3,-4,-5,6,-7,6,6,6,33,6,6,38,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,6,6,6,6,43,6,-13,6,6,6,-12,-6,-9,6,-11,-26,6,-8,-10,-27,-25,]),'NAME':([0,2,3,4,5,6,7,9,10,11,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,35,37,38,40,42,43,45,48,49,51,53,54,55,56,58,59,63,64,],[7,7,-3,-4,-5,7,-7,7,7,7,7,7,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,7,7,7,7,7,-13,7,48,7,7,53,-12,48,-6,-9,7,-11,-26,7,-8,-10,-27,-25,]),'$end':([1,2,3,4,5,7,8,35,45,49,51,54,55,58,59,63,],[0,-2,-3,-4,-5,-7,-1,-13,-12,-6,-9,-11,-26,-8,-10,-27,]),'RPAREN':([2,3,4,5,7,8,14,35,36,39,41,44,45,46,47,48,49,50,51,52,54,55,57,58,59,60,61,62,63,],[-2,-3,-4,-5,-7,-1,35,-13,45,49,51,54,-12,55,56,-29,-6,58,-9,59,-11,-26,-28,-8,-10,62,63,64,-27,]),'IF':([6,],[10,]),'WHILE':([6,],[11,]),'SET':([6,],[12,]),'LET':([6,],[13,]),'BEGIN':([6,],[15,]),'DEFINE':([6,],[16,]),'LAMBDA':([6,],[17,]),'PLUS':([6,],[18,]),'MUL':([6,],[19,]),'MINUS':([6,],[20,]),'AND':([6,],[21,]),'OR':([6,],[22,]),'EQ':([6,],[23,]),'LESS':([6,],[24,]),'LESSEQ':([6,],[25,]),'GREATER':([6,],[26,]),'GREATEREQ':([6,],[27,]),'NOT':([6,],[28,]),'EXCLAMATION':([12,],[32,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expressions':([0,2,6,15,34,],[1,8,14,36,44,]),'expression':([0,2,6,9,10,11,15,16,29,30,31,32,34,37,40,42,53,56,],[2,2,2,29,30,31,2,37,39,40,41,42,2,46,50,52,60,61,]),'op':([6,],[9,]),'binding':([13,],[34,]),'params':([38,48,],[47,57,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expressions","S'",1,None,None,None),
  ('expressions -> expression expressions','expressions',2,'p_program','parser.py',89),
  ('expressions -> expression','expressions',1,'p_program_empty','parser.py',93),
  ('expression -> INTEGER','expression',1,'p_expression_int','parser.py',97),
  ('expression -> TRUE','expression',1,'p_expression_bool','parser.py',101),
  ('expression -> FALSE','expression',1,'p_expression_bool','parser.py',102),
  ('expression -> LPAREN op expression expression RPAREN','expression',5,'p_expression_prim','parser.py',107),
  ('expression -> NAME','expression',1,'p_expression_var','parser.py',111),
  ('expression -> LPAREN IF expression expression expression RPAREN','expression',6,'p_expression_if','parser.py',115),
  ('expression -> LPAREN WHILE expression expression RPAREN','expression',5,'p_expression_while','parser.py',119),
  ('expression -> LPAREN SET EXCLAMATION expression expression RPAREN','expression',6,'p_expression_set','parser.py',123),
  ('expression -> LPAREN LET binding expressions RPAREN','expression',5,'p_expression_let','parser.py',127),
  ('expression -> LPAREN BEGIN expressions RPAREN','expression',4,'p_expression_begin','parser.py',131),
  ('expression -> LPAREN expressions RPAREN','expression',3,'p_expression_application','parser.py',135),
  ('op -> PLUS','op',1,'p_op','parser.py',139),
  ('op -> MUL','op',1,'p_op','parser.py',140),
  ('op -> MINUS','op',1,'p_op','parser.py',141),
  ('op -> AND','op',1,'p_op','parser.py',142),
  ('op -> OR','op',1,'p_op','parser.py',143),
  ('op -> EQ','op',1,'p_op','parser.py',144),
  ('op -> LESS','op',1,'p_op','parser.py',145),
  ('op -> LESSEQ','op',1,'p_op','parser.py',146),
  ('op -> GREATER','op',1,'p_op','parser.py',147),
  ('op -> GREATEREQ','op',1,'p_op','parser.py',148),
  ('op -> NOT','op',1,'p_op','parser.py',149),
  ('binding -> LPAREN LPAREN NAME expression RPAREN RPAREN','binding',6,'p_binding','parser.py',153),
  ('expression -> LPAREN DEFINE expression expression RPAREN','expression',5,'p_define','parser.py',157),
  ('expression -> LPAREN LAMBDA LPAREN params RPAREN expression RPAREN','expression',7,'p_lambda','parser.py',161),
  ('params -> NAME params','params',2,'p_params','parser.py',165),
  ('params -> NAME','params',1,'p_params_single','parser.py',169),
]
