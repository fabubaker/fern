using System.Runtime.Serialization;

namespace SeedEnum;

public enum Operand
{
    [EnumMember(Value = ">")]
    GreaterThan,

    [EnumMember(Value = "=")]
    EqualTo,

    [EnumMember(Value = "less_than")]
    LessThan
}
