using System.Text.Json.Serialization;

namespace SeedTrace;

public class LightweightStackframeInformation
{
    [JsonPropertyName("numStackFrames")]
    public int NumStackFrames { get; init; }

    [JsonPropertyName("topStackFrameMethodName")]
    public string TopStackFrameMethodName { get; init; }
}
