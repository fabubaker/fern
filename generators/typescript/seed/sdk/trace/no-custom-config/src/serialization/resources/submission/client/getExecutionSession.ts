/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../..";
import * as SeedTrace from "../../../../api";
import * as core from "../../../../core";

export const Response: core.serialization.Schema<
    serializers.submission.getExecutionSession.Response.Raw,
    SeedTrace.ExecutionSessionResponse | undefined
> = core.serialization.lazyObject(async () => (await import("../../..")).ExecutionSessionResponse).optional();

export declare namespace Response {
    type Raw = serializers.ExecutionSessionResponse.Raw | null | undefined;
}