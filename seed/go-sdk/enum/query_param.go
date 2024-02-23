// This file was auto-generated by Fern from our API Definition.

package enum

type SendEnumAsQueryParamRequest struct {
	Operand             Operand         `json:"-" url:"operand,omitempty"`
	MaybeOperand        *Operand        `json:"-" url:"maybeOperand,omitempty"`
	OperandOrColor      *ColorOrOperand `json:"-" url:"operandOrColor,omitempty"`
	MaybeOperandOrColor *ColorOrOperand `json:"-" url:"maybeOperandOrColor,omitempty"`
}

type SendEnumListAsQueryParamRequest struct {
	Operand             []Operand         `json:"-" url:"operand,omitempty"`
	MaybeOperand        []*Operand        `json:"-" url:"maybeOperand,omitempty"`
	OperandOrColor      []*ColorOrOperand `json:"-" url:"operandOrColor,omitempty"`
	MaybeOperandOrColor []*ColorOrOperand `json:"-" url:"maybeOperandOrColor,omitempty"`
}
