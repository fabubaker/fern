using System.Text.Json.Serialization;
using SeedTrace;

namespace SeedTrace.V2;

public class GetFunctionSignatureResponse
{
    [JsonPropertyName("functionByLanguage")]
    public Dictionary<Language, string> FunctionByLanguage { get; init; }
}
