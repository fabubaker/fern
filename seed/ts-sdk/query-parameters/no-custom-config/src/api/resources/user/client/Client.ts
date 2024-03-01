/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as core from "../../../../core";
import * as SeedQueryParameters from "../../..";
import * as serializers from "../../../../serialization";
import urlJoin from "url-join";
import * as errors from "../../../../errors";

export declare namespace User {
    interface Options {
        environment: core.Supplier<string>;
    }

    interface RequestOptions {
        timeoutInSeconds?: number;
        maxRetries?: number;
    }
}

export class User {
    constructor(protected readonly _options: User.Options) {}

    public async getUsername(
        request: SeedQueryParameters.GetUsersRequest,
        requestOptions?: User.RequestOptions
    ): Promise<SeedQueryParameters.User> {
        const {
            limit,
            id,
            date,
            deadline,
            bytes,
            user,
            keyValue,
            optionalString,
            nestedUser,
            optionalUser,
            excludeUser,
            filter,
        } = request;
        const _queryParams: Record<string, string | string[] | object | object[]> = {};
        _queryParams["limit"] = limit.toString();
        _queryParams["id"] = id;
        _queryParams["date"] = date;
        _queryParams["deadline"] = deadline.toISOString();
        _queryParams["bytes"] = bytes;
        _queryParams["user"] = await serializers.User.jsonOrThrow(user, {
            unrecognizedObjectKeys: "passthrough",
            allowUnrecognizedUnionMembers: true,
            allowUnrecognizedEnumValues: true,
            breadcrumbsPrefix: ["request", "user"],
        });
        _queryParams["keyValue"] = JSON.stringify(keyValue);
        if (optionalString != null) {
            _queryParams["optionalString"] = optionalString;
        }

        _queryParams["nestedUser"] = await serializers.NestedUser.jsonOrThrow(nestedUser, {
            unrecognizedObjectKeys: "passthrough",
            allowUnrecognizedUnionMembers: true,
            allowUnrecognizedEnumValues: true,
            breadcrumbsPrefix: ["request", "nestedUser"],
        });
        if (optionalUser != null) {
            _queryParams["optionalUser"] = await serializers.User.jsonOrThrow(optionalUser, {
                unrecognizedObjectKeys: "passthrough",
                allowUnrecognizedUnionMembers: true,
                allowUnrecognizedEnumValues: true,
                breadcrumbsPrefix: ["request", "optionalUser"],
            });
        }

        if (Array.isArray(excludeUser)) {
            _queryParams["excludeUser"] = await Promise.all(
                excludeUser.map(
                    async (item) =>
                        await serializers.User.jsonOrThrow(item, {
                            unrecognizedObjectKeys: "passthrough",
                            allowUnrecognizedUnionMembers: true,
                            allowUnrecognizedEnumValues: true,
                            breadcrumbsPrefix: ["request", "excludeUser"],
                        })
                )
            );
        } else {
            _queryParams["excludeUser"] = await serializers.User.jsonOrThrow(excludeUser, {
                unrecognizedObjectKeys: "passthrough",
                allowUnrecognizedUnionMembers: true,
                allowUnrecognizedEnumValues: true,
                breadcrumbsPrefix: ["request", "excludeUser"],
            });
        }

        if (Array.isArray(filter)) {
            _queryParams["filter"] = filter.map((item) => item);
        } else {
            _queryParams["filter"] = filter;
        }

        const _response = await core.fetcher({
            url: urlJoin(await core.Supplier.get(this._options.environment), "/user"),
            method: "GET",
            headers: {
                "X-Fern-Language": "JavaScript",
                "X-Fern-SDK-Name": "",
                "X-Fern-SDK-Version": "0.0.1",
                "X-Fern-Runtime": core.RUNTIME.type,
                "X-Fern-Runtime-Version": core.RUNTIME.version,
            },
            contentType: "application/json",
            queryParameters: _queryParams,
            timeoutMs: requestOptions?.timeoutInSeconds != null ? requestOptions.timeoutInSeconds * 1000 : 60000,
            maxRetries: requestOptions?.maxRetries,
        });
        if (_response.ok) {
            return await serializers.User.parseOrThrow(_response.body, {
                unrecognizedObjectKeys: "passthrough",
                allowUnrecognizedUnionMembers: true,
                allowUnrecognizedEnumValues: true,
                breadcrumbsPrefix: ["response"],
            });
        }

        if (_response.error.reason === "status-code") {
            throw new errors.SeedQueryParametersError({
                statusCode: _response.error.statusCode,
                body: _response.error.body,
            });
        }

        switch (_response.error.reason) {
            case "non-json":
                throw new errors.SeedQueryParametersError({
                    statusCode: _response.error.statusCode,
                    body: _response.error.rawBody,
                });
            case "timeout":
                throw new errors.SeedQueryParametersTimeoutError();
            case "unknown":
                throw new errors.SeedQueryParametersError({
                    message: _response.error.errorMessage,
                });
        }
    }
}