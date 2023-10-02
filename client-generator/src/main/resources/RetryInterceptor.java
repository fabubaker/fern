import java.io.IOException;
import java.time.Duration;
import java.util.Optional;
import java.util.Random;
import okhttp3.Interceptor;
import okhttp3.Response;

public class RetryInterceptor implements Interceptor {

    private static final Duration ONE_SECOND = Duration.ofSeconds(1);
    private final ExponentialBackoff backoff;
    private final Random random = new Random();

    public RetryInterceptor(int maxRetries) {
        this.backoff = new ExponentialBackoff(maxRetries);
    }

    @Override
    public Response intercept(Chain chain) throws IOException {
        Response response = chain.proceed(chain.request());

        if (shouldRetry(response.code())) {
            return retryChain(chain);
        }

        return response;
    }

    private Response retryChain(Chain chain) throws IOException {
        Optional<Duration> nextBackoff = this.backoff.nextBackoff();

        while (nextBackoff.isPresent()) {
            try {
                Thread.sleep(nextBackoff.get().toMillis());
            } catch (InterruptedException e) {
                throw new IOException("Interrupted while trying request", e);
            }
            Response response = chain.proceed(chain.request());
            if (shouldRetry(response.code())) {
                nextBackoff = this.backoff.nextBackoff();
            } else {
                return response;
            }
        }

        throw new IOException("Max retries reached");
    }

    private static boolean shouldRetry(int statusCode) {
        return statusCode == 408
                || statusCode == 409
                || statusCode == 429
                || statusCode >= 500;
    }

    private final class ExponentialBackoff {

        private final int maxNumRetries;

        private int retryNumber = 0;

        ExponentialBackoff(int maxNumRetries) {
            this.maxNumRetries = maxNumRetries;
        }

        public Optional<Duration> nextBackoff() {
            retryNumber += 1;
            if (retryNumber > maxNumRetries) {
                return Optional.empty();
            }

            int upperBound = (int) Math.pow(2, retryNumber);
            return Optional.of(ONE_SECOND.multipliedBy(random.nextInt(upperBound)));
        }
    }
}
